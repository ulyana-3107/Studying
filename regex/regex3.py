import re


def delete_extra_tag(text: str) -> str:
    reg1 = r'<div(?:(?!<div).)*?</div>'
    reg2 = r'<div.+</div>'

    simple_div = re.findall(reg1, text, flags=re.DOTALL)
    to_delete = [var for var in simple_div if 'span' not in var]
    for del_elem in to_delete:
        text = text.replace(del_elem, '')

    other_div = re.search(reg2, text, flags=re.MULTILINE|re.DOTALL)
    if other_div:
        a, b = other_div.span()
        if 'span' not in text[a: b]:
            del_part = text[a: b]
            text = text.replace(del_part, '')

    return text


if __name__ == '__main__':
    # test cases
    text1 = '''<div id=""leftcol""><div>Test</div> Some text</div>
        <div><div id=""tagcloud"">
            <span class=""mytags""><a href="""">tag1</a></span>
            <span class=""mytags""><a href="""">tag2</a></span>
            <!-- and a few more spans <div>Test2 bla2</div> of the same type -->
        </div>
        Some text</div>'''
    # <div>Test</div> должен быть удалён.

    text2 = '''<div id=""leftcol""><div>Test</div><span>Test</span> Some text</div>
        <div><div id=""tagcloud"">
            <span class=""mytags""><a href="""">tag1</a></span>
            <span class=""""mytags""""><a href="""">tag2</a></span>
            <!-- and a few more spans of the same type -->
        </div>
        Some text</div>'''
    # <div>Test</div> должен быть удалён.

    text3 = '''<div><div><div></div></div></div>'''
    # Дожно удалиться полностью