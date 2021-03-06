import time
from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import ui.main_window as main_window
import ui.dialog as dialog
import ui.contents_dialog as contents_dialog

import directory_crawler
import database as db
import time
import image_processing as ip
import tesseract
import filter
import debug
from debug import logger

DEBUG_OCR_DB = True
db.DEBUG_DATABASE = True
logger.setLevel(debug.logging.DEBUG)


if not DEBUG_OCR_DB:
    logger.setLevel(debug.logging.INFO)

#flags
RUN_OCR_THREAD = False

crop_mode = False

class main_gui(QtGui.QMainWindow, main_window.Ui_MainWindow):

	loaded_database = {}

	def __init__(self, parent=None):
		super(main_gui, self).__init__(parent)
		self.setupUi(self)

		self.folderSelect.clicked.connect(self.get_directory)
		self.runOCR.clicked.connect(self.open_dialog)
		self.matchList.itemDoubleClicked.connect(self.open_contents_dialog)

		self.dialog = None
		self.directory = None
		self.load_database()
		self.searchBar.textEdited.connect(self.search)
		self.radioHigh.clicked.connect(self.set_quality)
		self.radioLow.clicked.connect(self.set_quality)
		self.checkMovingCrop.clicked.connect(self.set_crop_mode)

	def get_directory(self):
		self.matchList.clear()
		self.directory = str(QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder"))
		print self.directory
		self.directoryBar.clear()
		self.directoryBar.insert(self.directory)

	def open_dialog(self):
		self.dialog = running_dialog(self.directory)
		self.hide()
		self.dialog.show()
		self.dialog.finished.connect(self.show_main_window)

	def open_contents_dialog(self):
		selected_item = self.matchList.selectedItems()[0].text()
		self.dialog = contents_window(self.loaded_database[str(selected_item)])
		self.dialog.show()

	def load_database(self):
		self.matchList.clear()
		with db.database() as database:
			rows = database.get_rows()	
			for row in rows:
				self.matchList.addItem(row[1])
				self.loaded_database.update({row[1]: row[2]})


	def set_quality(self):
		ip.dpi = 600
		if self.radioLow.isChecked():
			ip.dpi = 300

		print "Quality set to %d." % ip.dpi

	def set_crop_mode(self):
		global crop_mode
		crop_mode = False
		if self.checkMovingCrop.isChecked():
			crop_mode = True

		print "Crop mode set to %s." % crop_mode

	def search(self):
		self.matchList.clear()
		for file_name in self.loaded_database:
			if str(self.searchBar.text()).upper() in str(file_name).upper() or str(self.searchBar.text()).upper() in self.loaded_database[str(file_name)].upper():
				self.matchList.addItem(file_name)

	def show_main_window(self):
		self.show()
		self.load_database()

class running_dialog(QtGui.QDialog, dialog.Ui_Dialog):

	time_elapsed = 0
    
	def __init__(self, directory, parent=None):
		super(running_dialog, self).__init__(parent)
		self.setupUi(self)
		self.stopButton.clicked.connect(self.reject)
		logger.debug("sup")

		# ocr thread
		global RUN_OCR_THREAD
		RUN_OCR_THREAD = True
		self.processing_thread = ocr_thread(directory)
		self.processing_thread.finished.connect(self.close_dialog)
		self.processing_thread.update_dialog.connect(self.update_dialog)
		self.processing_thread.start()
		
		# timer
		self.run_timer = QtCore.QTimer()
		self.run_timer.timeout.connect(self.update_time_elapsed)
		self.run_timer.start(1000)

	def update_dialog(self):
		self.currentTask.setText(self.processing_thread.current_task)
		self.currentFile.setText(self.processing_thread.current_file)
		self.filesProcessed.setText(self.processing_thread.files_processed)
		self.timeRemaining.setText(self.processing_thread.time_remaining)
		self.progressBar.setValue(self.processing_thread.percent_complete)

	def update_time_elapsed(self):
		self.time_elapsed += 1
		time_string = time.strftime('%H:%M:%S', time.gmtime(self.time_elapsed))
		self.elapsedTime.setText("Elapsed Time: %s" % time_string)

	def reject(self):
		self.stop_processing_thread()

	def stop_processing_thread(self):
		global RUN_OCR_THREAD
		RUN_OCR_THREAD = False
		self.currentTask.setText("Stopping OCR...")

	def close_dialog(self):
		self.run_timer.stop()
		super(running_dialog, self).reject()

class contents_window(QtGui.QDialog, contents_dialog.Ui_contentsDialog):

	def __init__(self, contents, parent=None):
		super(contents_window, self).__init__(parent)
		self.setupUi(self)
		self.contentsBox.setPlainText(contents)


class ocr_thread(QtCore.QThread):
	""" Performs OCR on pdf's found in chosen directory.

	get input pdf --> get first page --> get first crop as tif --> run tesseract on crop --> repeat
	
	"""
	update_dialog = QtCore.pyqtSignal()

	current_task = "doing nothing"
	current_file = "Current File: "
	files_processed = "Files Processed: "
	elapsed_time = "Elapsed Time: "
	time_remaining = "Estimated Remaining: "
	percent_complete = 0

	def __init__(self, directory, parent=None):
		self.directory = directory
		super(ocr_thread, self).__init__(parent)

	def run(self):
		global RUN_OCR_THREAD
		
		self.current_task = "Scanning for PDFs..."
		self.update_dialog.emit()
		crawler = directory_crawler.crawler(self.directory)
		pdf_list = crawler.crawl()
		logger.debug("Directory crawler found a total of %d pdfs." % len(pdf_list))

		if RUN_OCR_THREAD:
			with db.database() as database:
				number_of_files_processed = 0
				total_files = len(pdf_list)
				
				for file in pdf_list:
					
					file_name = file.split("\\")[-1]
					if not RUN_OCR_THREAD:
						break

					if database.search(file_name):
						logger.debug("File already in database, skipping")
						number_of_files_processed += 1
						continue				

					self.files_processed = "Files Processed: %d of %d" % (number_of_files_processed, total_files) 
					self.current_file = "Current File: %s" % file_name
					self.update_dialog.emit()
					
					pdf = ip.pdf(file_name, file)

					for page_number in range(pdf.number_of_pages):
						if not RUN_OCR_THREAD:
							break
						with ip.pdf_page(pdf, page_number) as page:

							contents = ""

							crop_width_percent = 100

							global crop_mode
							if crop_mode:
								crop_height_percent = 20
								crop_height_px = int((float(crop_height_percent) / 100) * page.height)
								offset_px = int(page.height * (float(crop_height_percent) / 100) / 2)
								offset_max = int((1 - (float(crop_height_percent) / 100)) * page.height)
								offsets = range(0, int(offset_max + crop_height_px), offset_px)

							else:
								crop_height_percent = 100
								offsets = [0]
							
							number_of_crops = len(offsets)

							self.current_task = "Converting PDF to tif..."
							self.update_dialog.emit()

							for crop_number, offset in enumerate(offsets):
								logger.debug("Processing crop %d out of %d" % (crop_number + 1, number_of_crops))
								if not RUN_OCR_THREAD:
									break

								
								with ip.tif_crop(page, crop_width_percent, crop_height_percent, 0, offset) as crop:
									self.current_task = "Running OCR on file..."
									self.update_dialog.emit()
									with tesseract.tesseract(crop) as ocr_processor:
										contents += " "
										contents += ocr_processor.process_ocr()

							if RUN_OCR_THREAD:
								filtering = filter.string_filter(contents)
								filtering.remove_excess_whitespace()
								contents = filtering.filtered_string
								database.insert_row(file_name, contents, file)
								number_of_files_processed += 1


					time.sleep(5)
	

def main():
	app = QtGui.QApplication(sys.argv)
	form = main_gui()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()


