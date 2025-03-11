from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import pykorbit
# form_class = uic.loadUiType(os.path.join(os.path.dirname(__file__), "mywindow.ui"))[0]
form_class = uic.loadUiType("/Users/isang-yong/Desktop/mywindow.ui")[0]

class MySignal(QObject):
    signal1 = pyqtSignal(str)

    def run(self):
        self.signal1.emit("hello world")

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
        self.setWindowTitle("bitcoin auto trader")
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)
        # self.setWindowIcon(QIcon("bitcoin.png")) // not wokring on mac

        # 버튼 클릭 이벤트 연결
        self.inquiryButton.clicked.connect(self.inquiry)

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price: float = pykorbit.get_current_price("BTC")

        price = round(price)  # 반올림
        strPrice: str = str(price)
        newPrice: str = ""
        if len(strPrice) > 3:
            for i in range(len(strPrice)):
                if i % 3 == 0 and i != 0:
                    newPrice += "," + strPrice[i]
                else:
                    newPrice += strPrice[i]
        self.currentPriceEdit.setText(newPrice)

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1_emitted")