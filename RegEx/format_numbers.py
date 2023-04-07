import re


def function(m) -> str:
    m = m[0]
    if len(m) <= 3:
        return m
    else:
        rest = len(m) % 3
        f_part = [m[: rest]] + list(',')
        s_part = m[rest:]
        parts = []
        curr = ''
        if len(s_part) <= 3:
            f_part.append(s_part)
        else:
            for i in range(len(s_part)):
                curr += s_part[i]
                if not (i + 1) % 3:
                    parts.append(curr)
                    curr = ''
                    if i != len(s_part) - 1:
                        parts.append(',')
            f_part.extend(parts)
        if f_part[0] == '':
            f_part = f_part[2:]
        return ''.join(f_part)


def new_text(text: str) -> str:
    return re.sub(r'\b\d+?\b', function, text)


text = '''12 мало 
лучше 123 
1234 почти 
12354 хорошо 
стало 123456 
супер 1234567'''
print(new_text(text))


def new_number(number: str) -> str:
    number = number[0]
    rest, arr = len(number) % 3, []
    if rest:
        arr.append(rest)
    else:
        arr.append(0)
    arr.append(len(number)//3 - 1)
    new_arr = []
    if arr[0]:
        part = ''
        for i in range(arr[0]):
            part += number[i]
        new_arr.append(part)
    if not arr[1]:
        part = ''
        for i in range(arr[0], len(number)):
            part += number[i]
        new_arr.append(part)
    else:
        start = arr[0]
        for i in range(arr[1] + 1):
            part = ''
            for j in range(3):
                part += number[start + j]
            new_arr.append(part)
            start += 3
    return ','.join(new_arr)


def function2(text: str) -> str:
    pat = r'(\d{1,3}(?:\d{3}){1,}\b)'
    return re.sub(pat, new_number, text)


text = '''12 мало 
лучше 123 
1234 почти 
12354 хорошо 
стало 123456 
супер 1234567'''

print(function2(text))