# 1. for 반복문: 정해진 횟수만큼 반복 실행

# 리스트를 이용한 for 반복문
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)  # apple, banana, orange 순서대로 출력

# range() 함수를 이용한 for 반복문
for i in range(5):  # 0부터 4까지 5번 반복
    print(i)  # 0, 1, 2, 3, 4 순서대로 출력

# range() 함수의 시작, 끝, 증가폭 설정
for i in range(1, 10, 2):  # 1부터 9까지 2씩 증가하며 반복
    print(i)  # 1, 3, 5, 7, 9 순서대로 출력

# 2. while 반복문: 조건이 참인 동안 반복 실행

count = 0
while count < 3:
    print("Hello")
    count += 1  # count 값을 1씩 증가시켜 반복 종료 조건을 만족시킴

# 3. for vs while

# for: 반복 횟수가 명확할 때 사용
# while: 특정 조건이 만족될 때까지 반복할 때 사용

# 4. range() 함수

# range(stop): 0부터 stop-1까지 숫자 시퀀스 생성
# range(start, stop): start부터 stop-1까지 숫자 시퀀스 생성
# range(start, stop, step): start부터 stop-1까지 step만큼 증가하는 숫자 시퀀스 생성
