from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bitcoin auto trader")
        self.setGeometry(200, 100, 800, 450)
        # self.setWindowIcon(QIcon("bitcoin.png")) // not wokring on mac
        
    def btn1_clicked(self):
        print("btn1 clicked")

    def btn2_clicked(self):
        print("btn2 clicked")
        