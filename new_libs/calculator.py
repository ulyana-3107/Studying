# 4. Написать маленькую библиотечку: файлик с классом Calculator и статическими методами plus(a: int, b:
# int) -> int minus(a: int, b: int) -> int multiply(a: int, b: int) -> int divide(a: int, b: int) -> int Написать скрипт,
# который работает с этой библиотечкой. А теперь считаем, что эти два файла не лежат в одной папке (и даже
# в проекте). Написать BASH-скрипт (unix и windows) (на вход подаётся путь к скрипту и путь в
# библиотечке), который сделает корректный запуск этого скрипта (чтобы import сработал корректно)


class Calculator:
    @staticmethod
    def plus(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def minus(a: int, b: int):
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> int:
        return a//b

