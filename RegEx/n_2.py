import re


# plan: 1) read text from file
# 2) fix regexp
# 3) "i" sees like id? (fix)


text = '…<a id="1234">Some text1</a>…98/76/5432…<a id="1234">Some text2</a>…98/76/5432…'

p = '<a id="\d{1,}">.+</a>'
print(re.search(p, text))


