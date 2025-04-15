# 클래스 정의

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #f-string문법으로 변수명 바로 넘김(python 3.6)
        print(f"[Person] ID: {self.id}, Name: {self.name}")
        


class Manager(Person):
    def __init__(self, id, name, title):
        #부모를 지칭하는 함수
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"[Manager] ID: {self.id}, Name: {self.name}, Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"[Employee] ID: {self.id}, Name: {self.name}, Skill: {self.skill}")


# 테스트 코드 (총 10개)

def run_tests():
    print("=== 테스트 시작 ===")
    # 테스트 1: Person 생성 및 출력
    p1 = Person(1, "Alice")
    p1.printInfo()

    # 테스트 2: Manager 생성 및 출력
    m1 = Manager(2, "Bob", "Team Leader")
    m1.printInfo()

    # 테스트 3: Employee 생성 및 출력
    e1 = Employee(3, "Charlie", "Python")
    e1.printInfo()

    # 테스트 4: Person 다수 생성
    p2 = Person(4, "David")
    p2.printInfo()

    # 테스트 5: Manager 다수 생성
    m2 = Manager(5, "Eve", "Director")
    m2.printInfo()

    # 테스트 6: Employee 다수 생성
    e2 = Employee(6, "Frank", "Java")
    e2.printInfo()

    # 테스트 7: Manager의 멤버 접근
    print(m1.title)

    # 테스트 8: Employee의 멤버 접근
    print(e1.skill)

    # 테스트 9: 상속 확인 isinstance
    print(isinstance(m1, Person))  # True
    print(isinstance(e1, Person))  # True

    # 테스트 10: 각 클래스별 printInfo 오버라이딩 확인
    persons = [p1, m1, e1]
    for person in persons:
        person.printInfo()

    print("=== 테스트 종료 ===")


# 테스트 실행
if __name__ == "__main__":
    run_tests()
