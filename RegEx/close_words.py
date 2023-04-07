import re


def func(text: str) -> str:
    pat = r'(олень(\b\w+\b){,5}.* заяц)'
    return re.search(pat, text)[0]


text = 'Да он олень, а не заяц!'
print(func(text))

