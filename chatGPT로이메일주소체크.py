import re

# 이메일 검증을 위한 정규 표현식
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# 이메일 주소 검사 함수
def validate_email(email):
    if re.match(email_pattern, email):
        return True
    return False

# 샘플 이메일 주소 리스트
sample_emails = [
    "test@example.com",       # 유효한 이메일
    "hello.world@domain.co.kr",  # 유효한 이메일
    "user123@subdomain.domain.com", # 유효한 이메일
    "invalid-email.com",      # 유효하지 않은 이메일
    "another@domain",         # 유효하지 않은 이메일
    "valid.email@subdomain.domain.com", # 유효한 이메일
    "@missingusername.com",   # 유효하지 않은 이메일
    "test@.com",              # 유효하지 않은 이메일
    "user@domain@domain.com", # 유효하지 않은 이메일
    "user@domain.com"         # 유효한 이메일
]

# 샘플 이메일 주소 검사
for email in sample_emails:
    is_valid = validate_email(email)
    print(f"{email}: {'★Valid' if is_valid else '☆Invalid'}")
