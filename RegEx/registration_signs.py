import re


text = '''С227НА777 
КУ22777 
Т22В7477 
М227К19У9 
 С227НА777 '''

numbers = [i.strip() for i in text.split('\n')]

private = r'[a-zA-Zа-яА-Я]\d{3}[А-Яа-яa-zA-Z]{2}\d{2,3}'
taxi = r'[a-zA-ZА-Яа-я]{2}\d{2}\d{3}'
regex_dict = {private: 'Private', taxi: 'Taxi'}

res = 'Fail'
results = {}
for n in numbers:
    for pat, name in regex_dict.items():
        if len(re.findall(pat, n)) != 0:
            results[n] = name
            break
        else:
            results[n] = res
print(results)

