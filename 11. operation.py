# 1. 정수 연산자

# 덧셈 (+)
a = 5
b = 3
result_add = a + b 
print(result_add)  # 8 출력

# 뺄셈 (-)
result_sub = a - b
print(result_sub)  # 2 출력

# 곱셈 (*)
result_mul = a * b
print(result_mul)  # 15 출력

# 나눗셈 (/)
result_div = a / b
print(result_div)  # 1.6666666666666667 출력 (실수형 결과 반환)

# 나머지 (%)
result_mod = a % b
print(result_mod)  # 2 출력

# 거듭제곱 (**)
result_pow = a ** b
print(result_pow)  # 125 출력

# 몫 (//)
result_floor_div = a // b
print(result_floor_div)  # 1 출력 (정수형 결과 반환)

# 2. 문자열 연산자

# 연결 (+)
str1 = "Hello, "
str2 = "world!"
result_concat = str1 + str2
print(result_concat)  # Hello, world! 출력

# 반복 (*)
str3 = "Python "
result_repeat = str3 * 3
print(result_repeat)  # Python Python Python 출력

# 특정 문자열 포함 여부 확인 (in)
str4 = "apple"
result_in = "p" in str4
print(result_in)  # True 출력

# 특정 문자열 포함 여부 확인 (not in)
result_not_in = "z" not in str4
print(result_not_in)  # True 출력

# 인덱싱 ([])
str5 = "banana"
result_indexing = str5[1] 
print(result_indexing)  # a 출력 (0부터 시작하는 인덱스)

# 슬라이싱 ([:])
result_slicing = str5[0:3] 
print(result_slicing)  # ban 출력 (0번째 인덱스부터 2번째 인덱스까지)
