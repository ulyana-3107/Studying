import re


t = '''<div id="leftcol"><div>Test</div><span>Test</span> Some text</div>
    <div><div id="tagcloud">
        <span class="mytags"><a href="""">tag1</a></span>
        <span class=""mytags""><a href="""">tag2</a></span>
        <!-- and a few more spans of the same type -->
    </div>
    Some text</div>'''


# <div>Test</div> должен быть удалён.
pat = r'<div[^div]*(?:(?!span)[^div]*)</div>'
print(re.sub(pat, '', t))



