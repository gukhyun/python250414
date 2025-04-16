import googlemaps
import pandas as pd

# 구글맵 API 키 설정
API_KEY = "AIzaSyDvoqb44X5GAUfKPuwTIkAFgXmZQBrfNTY"  # 발급받은 API 키를 입력하세요
gmaps = googlemaps.Client(key=API_KEY)

# 신주쿠 중심 좌표
location = (35.6895, 139.6917)  # 신주쿠의 위도와 경도

# 반경 500m 내 음식점 검색
places_result = gmaps.places_nearby(
    location=location,
    radius=500,  # 반경 500m
    type="restaurant"  # 음식점
)

# 결과 정리
restaurants = []
for place in places_result["results"]:
    place_id = place.get("place_id")  # 장소 ID
    name = place.get("name")  # 음식점 이름
    rating = place.get("rating", "N/A")  # 평점
    address = place.get("vicinity")  # 주소
    link = f"https://www.google.com/maps/place/?q=place_id:{place_id}"  # 구글맵 링크

    # Place Details API 호출
    details = gmaps.place(place_id=place_id, fields=["name", "price_level", "reviews"])
    price_level = details.get("result", {}).get("price_level", "N/A")  # 가격대
    reviews = details.get("result", {}).get("reviews", [])  # 리뷰 목록

    # 대표 메뉴 추출 (첫 번째 리뷰에서 추출)
    if reviews:
        representative_menu = reviews[0].get("text", "N/A")  # 첫 번째 리뷰 텍스트
    else:
        representative_menu = "N/A"

    # 데이터 추가
    restaurants.append({
        "이름": name,
        "평점": rating,
        "가격대": price_level,
        "대표 메뉴": representative_menu,
        "주소": address,
        "링크": link
    })

# 데이터프레임 생성
df = pd.DataFrame(restaurants)

# 결과 출력
print(df)

# CSV 파일로 저장
df.to_csv("신주쿠_음식점_500m_API_세부정보.csv", index=False, encoding="utf-8-sig")
print("신주쿠 음식점 데이터를 '신주쿠_음식점_500m_API_세부정보.csv' 파일로 저장했습니다.")