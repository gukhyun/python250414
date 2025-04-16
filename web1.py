# web1.py
# 웹 크롤링을 위한 선언
from bs4 import BeautifulSoup
import requests

# 웹페이지를 로딩
page = open('chap09_test.html', 'rt', encoding='utf-8').read()
# beautifulsoup 객체 생성
soup = BeautifulSoup(page, 'html.parser')
# 전체페에지를 출력
# print(soup.prettify())
# # <p> 태그를 모두 찾기
# print(soup.find_all('p'))
# <p> 태그의 첫 번째 요소를 찾기

#최근에는 attrs속성 검색
print(soup.find_all("p", attrs={"class":"outer-text"}))

# <p> 태그의 text속성 검색: 태그 내부의 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    title = tag.text
    title = title.replace("\n", "")  # 줄바꿈 제거
    title = title.replace("\t", "")  # 탭 제거  
    print(title)
