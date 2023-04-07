import re

# task: Дан html-файл. Удалить все теги <div>, внутри них нет тега <span>.
# "1. Плохо протестировано:
# Mistakes
# <div id=""leftcol""><div>Test</div> Some text</div>
#     <div><div id=""tagcloud"">
#         <span class=""mytags""><a href="""">tag1</a></span>
#         <span class=""mytags""><a href="""">tag2</a></span>
#         <!-- and a few more spans of the same type -->
#     </div>
#     Some text</div>"


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
text2 = '''<div id=""leftcol""><div>Test</div> Some text</div>
     <div><div id=""tagcloud"">
         <span class=""mytags""><a href="""">tag1</a></span>
         <span class=""mytags""><a href="""">tag2</a></span>
         <!-- and a few more spans of the same type -->
     </div>
     Some text</div>"'''


print(redundant_div_del(text2))
