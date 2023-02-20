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