from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os
import pykorbit
# form_class = uic.loadUiType(os.path.join(os.path.dirname(__file__), "mywindow.ui"))[0]
form_class = uic.loadUiType("/Users/isang-yong/Desktop/mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
        self.setWindowTitle("bitcoin auto trader")
        # self.setWindowIcon(QIcon("bitcoin.png")) // not wokring on mac

        # 버튼 클릭 이벤트 연결
        self.inquiryButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price: float = pykorbit.get_current_price("BTC")
        price = round(price)  # 반올림
        print(price)
        strPrice: str = str(price)
        # 1000단위 이상이면 1000단위마다 컴마찍어서 구분하기
        # if len(strPrice) > 3:
        print(strPrice)
        newPrice: str = ""
        if len(strPrice) > 3:
            for i in range(len(strPrice)):
                if i % 3 == 0 and i != 0:
                    newPrice += "," + strPrice[i]
                else:
                    newPrice += strPrice[i]
        self.currentPriceEdit.setText(newPrice)