# demoForm9.py 
# demoForm9.ui(화면단) + demoForm9.py(로직단) 

#QyQt5 선언 
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웹 크롤링을 위한 선언
from bs4 import BeautifulSoup
# 웹 서버에 요청 선언
import urllib.request
#정규표현식 사용
import re

#디자인한 파일을 로딩(demoForm9.ui) 
form_class = uic.loadUiType("demoForm9.ui")[0]

#폼클래스를 정의(QMainWindow클래스를 상속)
class DemoForm(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) #UI설정 
    #슬롯메서드를 정의
    def firstClick(self): 
        #파일로 저장
        f=  open("clien.txt", "wt", encoding="utf-8")

        #페이지 처리
        for i in range(0, 10):
            # 페이지 번호를 0부터 9까지 반복하여 요청
            # 페이지 번호에 따라 URL이 달라짐
            # https://www.clien.net/service/board/sold&od=T31&category=0&po=0
            # https://www.clien.net/service/board/sold&od=T31&category=0&po=1
            # https://www.clien.net/service/board/sold&od=T31&category=0&po=2
            # https://www.clien.net/service/board/sold&od=T31&category=0&po=3
            url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
            print(url)
            #url = "https://www.clien.net/service/board/sold"
            response = urllib.request.urlopen(url)
            page = response.read().decode("utf-8", 'ignore')
            # 검색이 용이한 객체 생성
            soup = BeautifulSoup(page, 'html.parser')
            list = soup.find_all("span", attrs={"data-role":"list-title-text"})
            for tag in list:
                title = tag.text.strip()  # 앞뒤 공백 제거
                if re.search("아이폰", title):
                    print(title)
                    f.write(title + "\n")
        # <span class="subject_fixed" data-role="list-title-text" title="아이패드 미니"
        # </span>

        f.close()

        self.label.setText("첫번째 버튼 클릭")
    def secondClick(self): 
        self.label.setText("두번째 버튼 클릭했습니다.")
    def thirdClick(self): 
        self.label.setText("세번째 버튼 클릭~~")

#직접 모듈을 실행했는지 진입점 체크 
if __name__ == "__main__": 
    app = QApplication(sys.argv) #QApplication 객체 생성 
    demoForm = DemoForm() #DemoForm 객체 생성 
    demoForm.show() #화면 출력 
    app.exec_() #이벤트 루프 시작