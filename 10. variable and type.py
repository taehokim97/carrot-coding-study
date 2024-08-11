# 저장: Ctrl + S
# 실행: F5

# 변수란? 데이터를 저장하는 공간
# 데이터가 저장된 공간에 붙은 포스트잇

# 1. 변수 선언 및 값 할당
# 변수 이름 = 값 형태로 변수를 선언하고 값을 할당합니다.
name = "Alice"     # 문자열 (String) 타입: 텍스트 데이터를 저장합니다. 큰따옴표("") 또는 작은따옴표('')로 묶습니다.
age = 30           # 정수 (Integer) 타입: 숫자 데이터 중 정수를 저장합니다.
height = 165.5     # 실수 (Float) 타입: 숫자 데이터 중 소수점을 포함하는 숫자를 저장합니다.
is_student = True  # 불리언 (Boolean) 타입: True 또는 False 값을 저장합니다. 참/거짓 판단에 사용됩니다.

# 2. 변수 값 출력
# print() 함수를 사용하여 변수에 저장된 값을 출력합니다.
print(name)       # Alice 출력
print(age)        # 30 출력
print(height)     # 165.5 출력
print(is_student) # True 출력

# 3. 변수 타입 확인
# type() 함수를 사용하여 변수에 저장된 값의 타입을 확인합니다.
print(type(name))       # <class 'str'> 출력 (문자열 타입)
print(type(age))        # <class 'int'> 출력 (정수 타입)
print(type(height))     # <class 'float'> 출력 (실수 타입)
print(type(is_student)) # <class 'bool'> 출력 (불리언 타입)

# 4. 변수 값 변경
# 변수에 새로운 값을 할당하여 값을 변경할 수 있습니다.
age = 31        # age 변수의 값을 30에서 31로 변경
print(age)      # 31 출력

# 5. 여러 변수 동시 선언 및 할당
# 쉼표(,)를 사용하여 여러 변수를 동시에 선언하고 값을 할당할 수 있습니다.
x, y, z = 10, 20, 30
print(x, y, z)  # 10 20 30 출력

# 6. 같은 값을 여러 변수에 할당
# 같은 값을 여러 변수에 동시에 할당할 수 있습니다.
a = b = c = 5
print(a, b, c)  # 5 5 5 출력
