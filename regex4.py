import re


#  Дан html-файл. Заменить теги <div> на <span>, если их id=”spannable”, а длина содержимого не больше 20 символов.


def div_span(text: str) -> str:
    pat_old = r'(?:(.*?<div.*id=[\'"]spannable[\'"].*?>)(.{,20})(.*</div>))'
    pat = r'(?:(.*?<)(div)(.*id=[\'"]spannable[\'"].*?>.{,20}.*</)(div>))'
    sub_pat = r'\1span\3span>'
    return re.sub(pat, sub_pat, text)


text = '''
<div id="spannable">hello</div>
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