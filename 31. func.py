# 1. 함수 정의: def 키워드 사용

# 함수 이름: add_numbers
# 매개변수: num1, num2 (함수에 전달되는 값을 저장하는 변수)
# 반환 값: num1 + num2 (return 문을 사용하여 함수 실행 결과를 반환)
def add_numbers(num1, num2):
    """
    두 숫자를 더하는 함수

    Args:
        num1: 첫 번째 숫자
        num2: 두 번째 숫자

    Returns:
        num1과 num2의 합
    """
    result = num1 + num2
    return result

# 2. 함수 호출: 함수 이름과 함께 필요한 값(인자) 전달

sum_result = add_numbers(3, 5)  # add_numbers 함수 호출, 3과 5를 인자로 전달
print(sum_result)  # 8 출력

# 3. 매개변수 기본값 설정: 매개변수에 기본값을 지정하여 함수 호출 시 인자를 생략할 수 있음

def greet(name="친구"):
    """
    주어진 이름으로 인사하는 함수

    Args:
        name: 인사할 이름 (기본값: '친구')
    """
    print("안녕하세요, " + name + "님!")

greet()            # 안녕하세요, 친구님! 출력
greet("Alice")     # 안녕하세요, Alice님! 출력

# 4. 가변 인자 (*args): 함수 호출 시 임의 개수의 인자를 전달받을 수 있음

def calculate_sum(*args):
    """
    여러 숫자의 합을 계산하는 함수

    Args:
        *args: 임의 개수의 숫자
    """
    total = 0
    for num in args:
        total += num
    return total

sum_result = calculate_sum(1, 2, 3, 4, 5)
print(sum_result)  # 15 출력

# 5. 키워드 인자 (**kwargs): 함수 호출 시 키-값 쌍 형태의 인자를 전달받을 수 있음

def print_info(**kwargs):
    """
    키-값 쌍 형태의 정보를 출력하는 함수

    Args:
        **kwargs: 임의 개수의 키-값 쌍
    """
    for key, value in kwargs.items():
        print(key + ": " + str(value))

print_info(name="Bob", age=25, city="London")
# name: Bob
# age: 25
# city: London 출력
