import re


# Удалить теги div, внутри них нет тега span

# pat = r'<div.*?(?:<div>.+?</div>)*.*</div>'
def del_div(text: str) -> str:
    pat_old = r'^<div(?:(?!<span).)*?</div>$'
    pat = r'<div[^div]*(?:(?!span)[^div]*)</div>'
    return re.sub(pat, '', text, flags=re.MULTILINE)


text = '''
<div id="leftcol"><div>Test</div> Some text</div>
    <div><div id="tagcloud">
        <span class="mytags"><a href="">tag1</a></span>
        <span class=""mytags""><a href="">tag2</a></span>
        <!-- and a few more spans of the same type -->
    </div>
    Some text</div>"'''


with open('html_3.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(text)

with open('html_3.txt', 'r', encoding='utf-8-sig') as reader:
    text = ''
    for l in reader.readlines():
        text += l

with open('html_3_result.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(del_div(text))

