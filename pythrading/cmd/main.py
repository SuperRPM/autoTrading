from PyQt5.QtWidgets import QApplication
import sys
import os

# 현재 파일의 상위 디렉토리(cmd)의 상위 디렉토리(프로젝트 루트)를 파이썬 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from internal.gui import qt  # pythrading 패키지 이름 제거

app = QApplication(sys.argv)

window = qt.MyWindow()
window.show()
app.exec_()