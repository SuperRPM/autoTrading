from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
label = QLabel("Hello, PyQt5")

# window = QWidget()
# window.show()

label.show()

app.exec_()