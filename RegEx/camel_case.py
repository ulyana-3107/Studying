import re


def replace(text: str) -> str:
    p = r'[A-Z][a-z]+[0-9]*'
    new = {}
    for i in re.finditer(p, text):
        if text[i.end()] != ' ':
            new[i[0]] = i[0] + '_'
    for k, v in new.items():
        text = re.sub(k, v, text)
    return text


text = '''MyVar17 = OtherVar + YetAnother2Var 
TheAnswerToLifeTheUniverseAndEverything = 42'''


print(replace(text))