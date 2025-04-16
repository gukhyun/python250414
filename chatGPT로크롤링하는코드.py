import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Naver 검색 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 요청 및 파싱
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 제목 추출
titles = soup.select('a.news_tit')

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active
ws.title = "News Titles"

# 헤더 작성
ws.append(["번호", "제목", "링크"])

# 뉴스 제목들 저장
for i, title in enumerate(titles, 1):
    ws.append([i, title.get_text(), title['href']])

# 파일 저장
wb.save("result.xlsx")
print("result.xlsx 파일로 저장 완료!")
