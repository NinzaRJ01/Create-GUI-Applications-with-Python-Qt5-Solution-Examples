from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg 
import sys

app = qtw.QApplication(sys.argv)
class IntroWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()#Intializing Super Class Object
        labelwgt = qtw.QLabel("PyQt is Awesome!!")
        # labelwgt.setAlignment(qtg.Qt.AlignCenter)
        self.setWindowTitle("PyQT Application")
        labelwgt.setAlignment(qtc.Qt.AlignCenter)
        self.setCentralWidget(labelwgt)
        self.setGeometry(0,0,500,500)
        self.show()

win = IntroWindow()
# win.show()
app.exec_()