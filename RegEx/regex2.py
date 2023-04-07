import re


def teg_a(text: str) -> list:
    pat = r'<a.*?id=[\'"](\d+)[\'"].*?>(.+?)</a>'
    matches = re.findall(pat, text, flags=re.DOTALL)
    result = []
    if len(matches):
        for k, v in matches:
            result.append(k + ' - ' + v)
    return result


text = '''
…<a id="1234">Some text1</a>…98/76/5432…<a id="1234lol">Some text2</a>…98/76/5432…
<a i="1234">Some text1</a>…
…<a id="567">text001111</a>
'''

with open('html_2.txt', 'w', encoding='utf-8-sig') as text_writer:
    text_writer.write(text)

with open('html_2.txt', 'r', encoding='utf-8-sig') as text_reader:
    text = ''
    for l in text_reader.readlines():
        text += l
    result = teg_a(text)

with open('html_2_result.txt', 'w', encoding='utf-8-sig') as result_writer:
    if len(result):
        for r in result:
            result_writer.write(r + '\n')