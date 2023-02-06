import re

# task: Дан html-файл. Удалить все теги <div>, внутри них нет тега <span>.


def redundant_div_del(text: str) -> str:
    found = re.findall(r'<div.+?</div>', text, flags=re.DOTALL)
    delete = [elem for elem in found if '<span' not in elem]
    for d in delete:
        text = text.replace(d, '')
    return text


text = '''<div id="leftcol"></div>
    <div id="tagcloud">
        <span class="mytags"><a href="">tag1</a></span>
        <span class="mytags"><a href="">tag2</a></span>
        <!-- and a few more spans of the same type -->
    </div>
    '''


print(redundant_div_del(text))
