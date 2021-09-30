from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(0,0,300,300)
window.show()
app.exec_()