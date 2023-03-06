import re


#  Дан html-файл. Заменить теги <div> на <span>, если их id=”spannable”, а длина содержимого не больше 20 символов.

def replace(m: str, pat: str) -> str:
    return re.sub(pat, r'<span\3></span>', m)


def div_span(text: str) -> str:
    d = {}
    pat = r'(<(div)(.*id=[\'"]spannable[\'"].*)></(div)>)'
    for tup in re.findall(pat, text):
        if len(tup[2]) <= 20:
            d[tup[0]] = replace(tup[0], pat)
    for k, v in d.items():
        text = re.sub(k, v, text)
    return text



text = '''
<div id="spannable"></div>
    <div id="tagcloud"></div>
    <div id="spannable"><a href="""">tag1</a></div>
'''

with open('html_4.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(text)

with open('html_4.txt', 'r', encoding='utf-8-sig') as reader:
    text = ''
    for l in reader.readlines():
        text += l

with open('html_4_results.txt', 'w', encoding='utf-8-sig') as writer:
    result = div_span(text)
    writer.write(result)