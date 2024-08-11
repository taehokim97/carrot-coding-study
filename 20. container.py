# 1. 리스트 (List)

# 리스트 생성: 대괄호([]) 안에 쉼표(,)로 구분하여 값을 저장합니다.
fruits = ["apple", "banana", "orange"]

# 리스트 요소 접근: 인덱스(0부터 시작)를 사용하여 요소에 접근합니다.
print(fruits[0])  # apple 출력

# 리스트 요소 변경: 인덱스를 사용하여 요소 값을 변경합니다.
fruits[1] = "grape"
print(fruits)  # ['apple', 'grape', 'orange'] 출력

# 리스트 메서드: 리스트에는 다양한 메서드가 있습니다.
fruits.append("kiwi")  # 리스트 끝에 요소 추가
print(fruits)  # ['apple', 'grape', 'orange', 'kiwi'] 출력

fruits.insert(1, "banana")  # 특정 위치에 요소 삽입
print(fruits)  # ['apple', 'banana', 'grape', 'orange', 'kiwi'] 출력

fruits.remove("grape")  # 특정 값을 가진 요소 삭제
print(fruits)  # ['apple', 'banana', 'orange', 'kiwi'] 출력

# 2. 딕셔너리 (Dictionary)

# 딕셔너리 생성: 중괄호({}) 안에 키-값 쌍을 쉼표(,)로 구분하여 저장합니다.
person = {"name": "Alice", "age": 30, "city": "Seoul"}

# 딕셔너리 값 접근: 키를 사용하여 값에 접근합니다.
print(person["name"])  # Alice 출력

# 딕셔너리 값 변경: 키를 사용하여 값을 변경합니다.
person["age"] = 31
print(person)  # {'name': 'Alice', 'age': 31, 'city': 'Seoul'} 출력

# 딕셔너리 메서드: 딕셔너리에도 다양한 메서드가 있습니다.
person["job"] = "developer"  # 새로운 키-값 쌍 추가
print(person)  # {'name': 'Alice', 'age': 31, 'city': 'Seoul', 'job': 'developer'} 출력

del person["city"]  # 특정 키-값 쌍 삭제
print(person)  # {'name': 'Alice', 'age': 31, 'job': 'developer'} 출력
