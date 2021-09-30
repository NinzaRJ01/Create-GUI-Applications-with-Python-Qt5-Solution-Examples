from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg 

import sys #importing system module

app = qtw.QApplication(sys.argv)
#window
qwin = qtw.QMainWindow()
#textEdit
textEdit=qtw.QTextEdit()
qwin.setCentralWidget(textEdit)

#MenuBar
menu = qwin.menuBar()
file_menu=menu.addMenu('File')
file_menu.addAction('Open')
file_menu.addAction('Save')
file_menu.addSeparator()
file_menu.addAction('Quit',qwin.close)





qwin.show()
app.exec_()