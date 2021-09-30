from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg 

import sys

app = qtw.QApplication(sys.argv)
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        #Q Main Window Constructor
        super().__init__()
        self.setGeometry(0,0,800,500)
        self.textEdit = qtw.QTextEdit()
        self.setCentralWidget(self.textEdit)
        menu = self.menuBar()
        openAction=menu.addMenu('Open')
        openAction.addAction('Open File').triggered.connect(self.open_file)
        self.show()
    def open_file(self):
        #getOpenFileName Return tuple in which for now second value of no worth
        filename, _ = qtw.QFileDialog.getOpenFileName()
        "Debug"
        # print("-------------"+str(filename))
        text=""
        if filename :
            with open(filename,'r') as file:
                text = file.read()
            self.textEdit.clear()
            self.textEdit.insertPlainText(text)
            self.textEdit.moveCursor(qtg.QTextCursor.Start)
win = MainWindow()
app.exec_()