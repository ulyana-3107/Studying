import re


text = '''КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII,
ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., ЛюдовикXVIII,
ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI'''

# Positive lookaround assertion
print(re.findall(r'Людовик(?=VI)', text))  # Людовик, но только если шестой

# Negative lookaround assertion
print(re.findall(r'Людовик(?!VI)', text))   # Людовик, но только если не шестой

# Positive lookbehind assertion
print(re.findall(r'(?<=Людовик)VI', text))  # Шестой, но только если людовик

# Negative lookbehind assertion
print(re.findall(r'(?<!Людовик)VI', text))  # Шестой, но только не Людовик
