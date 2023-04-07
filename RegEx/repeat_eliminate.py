import re


def function(text: str) -> str:
    pat = r'(?:([А-Яа-я]+)\s(\1))'
    return re.sub(pat, r'\1', text)


text = '''Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? 
Не нужно портить хор хоровод.'''


print(function(text))
