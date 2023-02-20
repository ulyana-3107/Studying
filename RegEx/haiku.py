import re


text = '''Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...; Просто текст ; Как вишня расцвела! / Она с 
коня согнала / И князя-гордеца.; На голой ветке / Ворон сидит одиноко… / Осенний вечер!; Тихо, тихо ползи, / 
Улитка, по склону Фудзи, / Вверх, до самых высот!; Жизнь скоротечна… / Думает ли об этом / Маленький мальчик.'''


strings = text.split(';')
for string in strings:
    new = re.sub('\s', '', string)
    print(f'string: {new}', end='\t\t-----')
    parts = re.split('/', new)
    if len(parts) != 3:
        print('Not Haiku!')
    else:
        pat = r'[уеыаоэяию]'
        res = [len(re.findall(pat, p, flags=re.IGNORECASE)) for p in parts]
        if res == [5, 7, 5]:
            print('Haiku!')
        else:
            print('Not Haiku!')