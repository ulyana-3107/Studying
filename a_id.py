import re


# То есть, например, для …<a id=”1234”>Some text</a>…
# Я ожидаю увидеть вывод:
# …
# 1234 – Some text


text = '…<a id="1234">Some text.txt</a>…98/76/5432…<a id="12345">Some text.txt</a>…98/76/5432…'
text_ = '<a class="b_hide" Id="111" href="" h="ID=SERP,5493.1">Random_text</a>'
text_0 = '<a class="b_hide" id="P334" href="" h="ID=SERP,5493.1"></a>'


with open('html.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(','.join([text, text_, text_0]))

with open('html.txt', 'r', encoding='utf-8-sig') as reader:
    text__ = reader.readline()


def function(text: str) -> list:
    pat = r'(?<=<a)(.*?[i|I][D|d]="\d+".*?)(?=</a)'
    pat2 = r'(?<=[i|I][d|D]=")(\d+)(?=".+)'
    pat3 = r'([i|I][d|d]="\d+">)'
    arr = []
    parts = re.findall(pat, text)
    for p in parts:
        arr.append(re.search(pat2, p)[0] + ' -' + re.sub(pat3, '', p))
    return arr


with open('html_results.txt', 'w', encoding='utf-8-sig') as res_writer:
    results = function(text__)
    for sub_str in results:
        res_writer.write(sub_str + '\n')