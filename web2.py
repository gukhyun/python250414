# web2.py
# 웹 크롤링을 위한 선언
from bs4 import BeautifulSoup

# 웹 서버에 요청 선언
import urllib.request

#정규표현식 사용
import re


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
