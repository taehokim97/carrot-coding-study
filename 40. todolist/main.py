# app.py 파일을 가져오기 위해 sys.path.append()를 사용하여 폴더를 추가해준다.
import sys
sys.path.append('32. todolist')

# python 3.12.4
import app


def main():
    database, handlers = app.init()
    while database[app.Columns.RUN]:
        command = app.get_command(database)
        handler = handlers.get(command, None)
        if handler is None:
            continue
        handler(database)
    return 0


if __name__ == "__main__":
    main()