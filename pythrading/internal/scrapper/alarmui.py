from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pybithumb
import sys
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils.numbersplit import make_comma
form_class = uic.loadUiType("/Users/isang-yong/Desktop/bullMarketAlarm.ui")[0]
tickers: list[str] = ["BTC", "ETH", "BCH", "ETC"]

class MyWindow(QMainWindow, form_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        timer = QTimer(self)
        timer.start(3000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        # 테이블 위젯 초기화
        self.tableWidget.setRowCount(len(tickers))
        self.tableWidget.setColumnCount(self.tableWidget.columnCount())  # UI에서 정의된 컬럼 수를 가져와서 설정
        
        # 데이터 설정
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, (item))

            price, last_ma5, state = self.get_market_infos(ticker)
            strPrice = make_comma(price)
            item = QTableWidgetItem(strPrice)
            self.tableWidget.setItem(i, 1, item)

            strLastMa5 = make_comma(last_ma5)
            item = QTableWidgetItem(strLastMa5)
            self.tableWidget.setItem(i, 2, item)

            item = QTableWidgetItem(state)
            self.tableWidget.setItem(i, 3, item)
        # UI 업데이트 강제
        self.tableWidget.viewport().update()

    def get_market_infos(self, ticker: str) -> tuple[float, float, str]:
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5.iloc[-2]
        price = df['close'].iloc[-1]

        state = None
        if price > last_ma5:
            state = "상승장"
        else:
            state = "하락장"
        
        return price, last_ma5, state
            
        
        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

