import time
from datetime import datetime
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import main_window

class main_gui(QtGui.QMainWindow, main_window.Ui_MainWindow):
	def __init__(self, parent=None):
		super(main_gui, self).__init__(parent)
		self.setupUi(self)

def main():
	app = QtGui.QApplication(sys.argv)
	form = main_gui()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()








