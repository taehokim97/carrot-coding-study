# NOTE! 파이썬에서 _로 시작하는 변수/함수는 다른 모듈에서 직접 호출하지 않는 것이 관례.
# 따라서 현재 app.py 에서 외부에 노출된 기능(인터페이스)은 Columns, Commands, init, get_command 이다.
# enum: 열거형 데이터 타입, 상수를 정의하는데 사용
import enum


# class: 사용자 정의 데이터 타입
# Database의 키값을 정의
class Columns(enum.Enum):
    RUN = enum.auto()
    COMMANDS = enum.auto()
    TODO = enum.auto()
    DONE = enum.auto()

# Command의 키값을 정의
class Commands(enum.Enum):
    KEY  = enum.auto()
    NAME = enum.auto()

def init():
    handlers = {}
    database = {
        Columns.RUN: True,
        Columns.COMMANDS: [],
        Columns.TODO: [],
        Columns.DONE: []
    }

    # globals(): 전역에 정의된 변수들을 딕셔너리 형태로 반환
    # NOTE! 함수는 객체이므로, 함수명은 변수명과 동일하게 취급된다.
    all_command_funcs = []
    for g_name, g_value in globals().items():
        # 만약, g_name이 "_command"로 시작한다면 command로 취급한다.
        # 이는 현재 프로그램에서의 규칙이다.
        if g_name.startswith("_command"):
            all_command_funcs.append(g_value)

    # Database에 모든 command 함수에 대한 정보를 등록한다.
    for command_func in all_command_funcs:
        key, name = _parse_command(command_func)
        database[Columns.COMMANDS].append({
            Commands.KEY: key,
            Commands.NAME: name
        })

    # Handler 딕셔너리에 모든 command 함수를 등록한다.
    for command_func in all_command_funcs:
        key, _ = _parse_command(command_func)
        handlers[key] = command_func

    return database, handlers


def get_command(database):
    # Database에 등록된 command 정보를 출력하고 사용자로부터 입력을 받는다.
    index = 1
    for command_dict in database[Columns.COMMANDS]:
        # [01] 프로그램 종료                  (exit)
        print(f"[{index:02d}] {command_dict[Commands.NAME]:<30}({command_dict[Commands.KEY]})")
        index += 1
    
    while True:
        user_input = input(" >>> ").strip()
        # 사용자의 입력이 숫자이며 적절한 인덱스 범위 안에 있다면, 반복문 탈출
        if user_input.isnumeric() and 1 <= int(user_input) < index:
            # 사용자의 입력이 숫자이므로, 해당 인덱스에 해당하는 Command Key로 변경한다.
            user_input = database[Columns.COMMANDS][int(user_input) - 1][Commands.KEY]
            break
        # 사용자의 입력이 Command Key에 해당한다면 반복문 탈출
        else:
            for command_dict in database[Columns.COMMANDS]:
                if user_input == command_dict[Commands.KEY]:
                    break
        # 위에서 반복문을 탈출하지 못했다면 사용자에게 잘못된 입력임을 알린다.
        print("Wrong Input, Please try again.")
    
    return user_input

def _parse_command(func):
    # 함수의 docstring을 파싱하여, key와 name 값을 추출한다.
    key, name = func.__doc__.split("|")
    return key.strip(), name.strip()

def _command_exit(database):
    # 함수 최상단에 작성된 문자열은 docstring 으로, 함수에 대한 설명을 담고 있다.
    # 현재 프로그램에서는 이를 메타 데이터로 사용한다.
    """
    exit |
    프로그램 종료
    """
    database[Columns.RUN] = False


def _command_add(database):
    """
    add |
    할 일 추가
    """
    todo = input(" >>> ").strip()
    database[Columns.TODO].append(todo)

    