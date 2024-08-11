# 1. if 문: 조건에 따라 코드 실행 여부 결정

x = 10
if x > 5:
    print("x는 5보다 큽니다.")  # x가 5보다 크므로 이 부분 실행

# 2. if-else 문: 조건에 따라 다른 코드 실행

y = 3
if y % 2 == 0:
    print("y는 짝수입니다.")
else:
    print("y는 홀수입니다.")  # y가 홀수이므로 이 부분 실행

# 3. if-elif-else 문: 여러 조건을 순차적으로 검사

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")  # score가 80 이상 90 미만이므로 이 부분 실행
elif score >= 70:
    print("C")
else:
    print("D")

# 4. break 문: 반복문 즉시 종료

for i in range(10):
    if i == 5:
        break  # i가 5가 되면 반복문 종료
    print(i)  # 0 1 2 3 4 출력

# 5. continue 문: 현재 반복 건너뛰고 다음 반복 실행

for j in range(10):
    if j % 2 == 0:
        continue  # j가 짝수면 다음 반복으로 넘어감
    print(j)  # 1 3 5 7 9 출력

# 6. 조건문 중첩: 조건문 안에 다른 조건문 사용 가능

age = 25
is_student = True

if age < 18:
    print("미성년자입니다.")
else:
    if is_student:
        print("성인이며 학생입니다.")  # age가 18 이상이고 is_student가 True이므로 이 부분 실행
    else:
        print("성인이며 학생이 아닙니다.")
