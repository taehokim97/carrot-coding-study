# 사용자는 친절한 사용자를 가정합니다.
# 배운 내용만을 사용하여 간단한 할 일 관리 프로그램을 만들어봅니다.
todo_list = []
done_list = []

count = input(">>> 몇 개의 할 일을 추가하시겠습니까? ")
count = int(count)

# 사용하지 않는 임시 변수는 _로 표시합니다.
for _ in range(count):
    todo = input(">>> 할 일을 입력하세요: ")
    todo_list.append(todo)
    print(f"새로운 할 일 {todo}를 추가했습니다.")

while todo_list:
    # enumerate() 함수를 사용하여 인덱스와 값을 함께 출력합니다.
    print(" === 현재 할 일 목록 === ")
    for i, todo in enumerate(todo_list):
        print(f"[{i}] {todo}")

    done_i = input(">>> 완료한 일의 인덱스를 입력하세요: ")
    done_i = int(done_i)

    if 0 <= done_i < len(todo_list):
        done = todo_list.pop(done_i)
        done_list.append(done)
        print(f"완료한 일 {done}를 이동했습니다.")
    
    print(" === 완료한 일 목록 === ")
    for done in done_list:
        print(f" - {done}")
    