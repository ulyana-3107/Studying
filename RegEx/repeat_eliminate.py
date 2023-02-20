import re


text = '''Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? 
Не нужно портить хор хоровод.'''


def repeat_eliminate(text: str) -> str:
    return re.sub(r'([а-яА-Я]+)\s(\1{1,})', r'\1', text)


print(repeat_eliminate(text))
