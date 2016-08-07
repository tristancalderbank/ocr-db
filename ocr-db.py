import time
from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import ui.main_window as main_window
import ui.dialogue as dialogue
import directory_crawler
import database as db
import time
import image_processing as ip

#flags
RUN_OCR_THREAD = False

class main_gui(QtGui.QMainWindow, main_window.Ui_MainWindow):

	matches = []

	def __init__(self, parent=None):
		super(main_gui, self).__init__(parent)
		self.setupUi(self)

		self.folderSelect.clicked.connect(self.get_directory)
		self.runOCR.clicked.connect(self.open_dialog)

		self.dialog = None
		self.directory = None
		self.load_database()

		self.searchBar.textEdited.connect(self.search)

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

	def load_database(self):
		with db.database() as database:
			rows = database.get_rows()	
			for row in rows:
				self.matches.append(row[1])
				self.matchList.addItem(row[1])	

	def search(self):
		self.matchList.clear()
		for item in self.matches:
			if str(self.searchBar.text()) in item:
				self.matchList.addItem(item) 		
		

	def show_main_window(self):
		self.show()

class running_dialog(QtGui.QDialog, dialogue.Ui_Dialog):
	def __init__(self, directory, parent=None):
		super(running_dialog, self).__init__(parent)
		self.setupUi(self)
		self.stopButton.clicked.connect(self.reject)

		global RUN_OCR_THREAD
		RUN_OCR_THREAD = True
		self.processing_thread = ocr_thread(directory)
		self.processing_thread.finished.connect(self.close_dialog)
		self.processing_thread.update_dialog.connect(self.update_dialog)
		self.processing_thread.start()

	def update_dialog(self):
		self.currentTask.setText(self.processing_thread.current_task)
		self.currentFile.setText(self.processing_thread.current_file)
		self.filesProcessed.setText(self.processing_thread.files_processed)
		self.elapsedTime.setText(self.processing_thread.elapsed_time)
		self.timeRemaining.setText(self.processing_thread.time_remaining)
		self.progressBar.setValue(self.processing_thread.percent_complete)

	def reject(self):
		self.stop_processing_thread()

	def stop_processing_thread(self):
		global RUN_OCR_THREAD
		RUN_OCR_THREAD = False
		self.currentTask.setText("Stopping OCR...")

	def close_dialog(self):	
		super(running_dialog, self).reject()
	
class ocr_thread(QtCore.QThread):

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
		
		if RUN_OCR_THREAD:	
			crawler = directory_crawler.crawler(self.directory)
			pdf_list = crawler.crawl()

		if RUN_OCR_THREAD:
			with db.database() as database:
				files_processed = 0
				for file in pdf_list:
					file_name = file.split("//")[-1]
					self.current_file = "Current File: %s" % file_name
					self.update_dialog.emit()
					
					#pdf = ip.pdf(file_name, file)
					time.sleep(5)
	

def main():
	app = QtGui.QApplication(sys.argv)
	form = main_gui()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
