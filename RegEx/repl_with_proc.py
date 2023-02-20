import re


# task: «зацензурим» все слова, начинающиеся на букву «Х»:

def replace(m) -> str:
    return '>censored(' + str(len(m[0])) + ')<'


text = 'Некоторые хорошие слова подозрительны: хор, хоровод, хороводоводовед.'
print(re.sub(r'\b[Хх]\w*', replace, text))