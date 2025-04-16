import random
from openpyxl import Workbook

# 전자제품 판매 데이터 생성
def generate_product_data(num_products=100):
    products = []
    product_names = [
        "Smartphone", "Laptop", "Tablet", "Smartwatch", "Headphones",
        "Camera", "Printer", "Monitor", "Keyboard", "Mouse"
    ]  # 실제 제품명 리스트

    product_counters = {name: 1 for name in product_names}  # 제품별 ID 카운터

    for _ in range(num_products):
        product_name = random.choice(product_names)  # 랜덤 제품명 선택
        product_id = f"{product_name[:3].upper()}{product_counters[product_name]:03d}"  # 제품 ID 생성
        product_counters[product_name] += 1  # ID 카운터 증가
        quantity = random.randint(1, 100)  # 수량 (1~100 랜덤)
        price = round(random.uniform(50.0, 5000.0), 2)  # 가격 (50.0~5000.0 랜덤)
        products.append((product_id, product_name, quantity, price))
    return products

# 데이터를 Excel 파일로 저장
def save_to_excel(file_name, data):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "전자제품리스트"

    # 헤더 작성
    headers = ["제품 ID", "제품명", "수량", "가격"]
    sheet.append(headers)

    # 데이터 작성
    for row in data:
        sheet.append(row)

    # 파일 저장
    workbook.save(file_name)

# 메인 함수
if __name__ == "__main__":
    file_name = "products.xlsx"  # 저장할 파일 이름
    product_data = generate_product_data()  # 데이터 생성
    save_to_excel(file_name, product_data)  # 데이터 저장
    print(f"데이터가 '{file_name}' 파일로 성공적으로 저장되었습니다.")