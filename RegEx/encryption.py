import re


def func(m) -> str:
    return str(int(float(m[0])**3))


def encrypt(t: str) -> str:
    pat = r'\d+\.?\d*'
    return re.sub(pat, func, t)


t = '''Было закуплено 12 единиц техники 
по 410.37 рублей.'''


print(encrypt(t))