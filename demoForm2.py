# demoForm.py
# demoForm.ui(화면단) + demoForm.py(로직단)
#QyQt5 선언
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인한 파일을 로딩
form_class = uic.loadUiType("demoForm2.ui")[0]

#폼클래스를 정의(QMainWindow를 상속받음)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 초기화
        
    #슬롯메서드를 정의
    def firstClick(self):
        self.label.setText("you click the 'First' button!") # 라벨에 문자열 출력
    def secondClick(self):
        self.label.setText("you click the 'Second' button!")
    def thirdClick(self):
        self.label.setText("you click the 'Third' button!")

#직접 모듈을 실행했는지 진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    demoForm = DemoForm()  # DemoForm 객체 생성
    demoForm.show()  # DemoForm 화면 출력
    app.exec_()  # 이벤트 루프 실행