import re

# task:Дан html-файл. Заменить теги <div> на <span>, если их id=”spannable”, а длина содержимого не больше 20 символов.


def replace(text: str) -> str:
    return re.sub(r'<(div)(.{,20})><(/div)>', r'<span\2></span>', text)


text = '''<div id="spannable"></div>
    <div id="tagcloud">
        <span class="mytags"><a href="">tag1</a></span>
        <span class="mytags"><a href="">tag2</a></span>
        <!-- and a few more spans of the same type -->
    </div>
    <div id="spannable"><span class="mytags"><a href="">tag1</a></span></div>
    '''


print(replace(text))