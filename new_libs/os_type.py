# 6. Написать скрипт, который будет определять, в какой ОС мы сейчас работаем и подгружать
# соответствующую библиотечку из пункта 5. Сделать пару вызовов из этой библиотеки.
# P.S. Ветвление if для этой задачи должно занимать не более 4 строчек. Считаем, что методы у классов
# (названия и параметры) абсолютно идентичные и отличаются только реализацией.
# То есть:
# if OS == "UNIX":
# Подгрузили
# else:
# Подгрузили
# Работаем с либой..
import platform
from unix import Unix
from windows import Windows
import argparse


def check_platform() -> str:
    return platform.system()


def main(path: str):
    if check_platform().lower() == 'windows':
        os = Windows(path)
    elif check_platform().lower() == 'unix':
        os = Unix(path)

    print(f'Current path: {os.get_curr_path()}')
    print(f'Root of dir tree: {os.get_root()}')
    path1 = input('Enter first path to join paths:')
    path2 = input('Enter second path to be joined:')
    np = os.join(path1, path2)
    print(f'New joined path: {np}')
    nwd = input('Enter a directory to move there:')
    os.cd(nwd)
    print(f'Current path after cd function: {os.get_curr_path()}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to work with ')
    parser.add_argument('path', type=str, help='Path to work with')
    args = parser.parse_args()
    main(args.path)