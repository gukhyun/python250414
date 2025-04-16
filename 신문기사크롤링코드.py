import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# URL 설정
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# HTTP 요청
response = requests.get(url)

# 응답 확인
if response.status_code == 200:
    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 기사 제목 크롤링
    titles = soup.select('a.news_tit')  # 뉴스 제목이 포함된 링크 태그 선택
    
    # 엑셀 파일 생성
    wb = Workbook()
    ws = wb.active
    ws.title = "뉴스 제목"
    
    # 헤더 추가
    ws.append(["번호", "제목"])
    
    # 제목 저장
    for idx, title in enumerate(titles, start=1):
        ws.append([idx, title.text.strip()])  # 번호와 제목을 엑셀에 추가
    
    # 엑셀 파일 저장
    wb.save("result.xlsx")
    print("크롤링 결과가 'result.xlsx' 파일로 저장되었습니다.")
else:
    print(f"HTTP 요청 실패. 상태 코드: {response.status_code}")