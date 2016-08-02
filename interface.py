import time
from datetime import datetime
from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import main_window
import dialogue

class main_gui(QtGui.QMainWindow, main_window.Ui_MainWindow):
	def __init__(self, parent=None):
		super(main_gui, self).__init__(parent)
		self.setupUi(self)
		self.folderSelect.clicked.connect(self.get_directory)
		self.runOCR.clicked.connect(self.open_dialog)
		self.dialog = None

	def get_directory(self):
		self.matchList.clear()
		directory = QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder")
		self.directoryBar.clear()
		self.directoryBar.insert(directory)

	def open_dialog(self):
		if self.dialog is None:
			self.dialog = running_dialog(self)
		self.dialog.stopButton.clicked.connect(self.show_main_window)
		self.hide()
		self.dialog.show()

	def show_main_window(self):
		self.show()

class running_dialog(QtGui.QDialog, dialogue.Ui_Dialog):
	def __init__(self, parent=None):
		super(running_dialog, self).__init__(parent)
		self.setupUi(self)
		self.stopButton.clicked.connect(self.close_dialog)

		
	def close_dialog(self):
		self.close()
		

def main():
	app = QtGui.QApplication(sys.argv)
	form = main_gui()
	form.show()
	app.exec_()
if __name__ == '__main__':
	main()
