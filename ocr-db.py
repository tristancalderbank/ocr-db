import time
from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import ui.main_window as main_window
import ui.dialogue as dialogue
import directory_crawler
import database as db
import time



class main_gui(QtGui.QMainWindow, main_window.Ui_MainWindow):

	def __init__(self, parent=None):
		super(main_gui, self).__init__(parent)
		self.setupUi(self)
		self.folderSelect.clicked.connect(self.get_directory)
		self.runOCR.clicked.connect(self.open_dialog)
		self.dialog = None
		self.directory = None

	def get_directory(self):
		self.matchList.clear()
		self.directory = str(QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder"))
		print self.directory
		self.directoryBar.clear()
		self.directoryBar.insert(self.directory)

	def open_dialog(self):
		if self.dialog is None:
			self.dialog = running_dialog(self.directory)
		self.dialog.stopButton.clicked.connect(self.show_main_window)
		self.hide()
		self.dialog.show()

	def show_main_window(self):
		self.show()

class running_dialog(QtGui.QDialog, dialogue.Ui_Dialog):
	def __init__(self, directory, parent=None):
		super(running_dialog, self).__init__(parent)
		self.setupUi(self)
		self.stopButton.clicked.connect(self.close_dialog)

		ocr_thread = ocr_thread(directory)
		ocr_thread.start()
	
	def close_dialog(self):
		self.close()

class ocr_thread(QtCore.QThread)	

	def __init__(self, directory):
		self.directory = directory
		self.update_dialog = QtCore.pyqtSignal()

	def run(self):
		crawler = directory_crawler.crawler(self.directory)
		pdf_list = crawler.crawl()

		with db.database() as database:
			for file in pdf_list:
				self.currentFile.setText("Current File: %s" % file)
				time.sleep(3)
		


def main():
	app = QtGui.QApplication(sys.argv)
	form = main_gui()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
