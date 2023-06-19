"""
Задача: Дан html-файл. Заменить теги <div> на <span>, если их id=”spannable”, а длина содержимого не больше 20 символов.
"""
import re


def replace_divs(text: str, len_limit: int = 20):
    div_reg = r"<\s*div(?:\s+[^>]*?)?>"
    div_end_reg = r"<\s*/div\s*>"
    reg = f"({div_reg})|({div_end_reg})"
    spannable_reg = r"\s+id\s*=\s*['\"]spannable['\"]"

    parts = re.split(reg, text)
    stack = [["", False, parts[0]]]
    for i in range(1, len(parts), 3):
        if parts[i]:
            stack.append([parts[i], re.search(spannable_reg, parts[i]) is not None, parts[i+2]])
        else:
            div_def, is_spannable, div_cont = stack.pop()
            if is_spannable and len(div_cont) <= len_limit:
                stack[-1][-1] += div_def.replace("div", "span", 1) + div_cont + parts[i+1].replace("div", "span", 1)
            else:
                stack[-1][-1] += div_def + div_cont + parts[i + 1]
            stack[-1][-1] += parts[i+2]
    return stack[0][-1]


if __name__ == "__main__":
    text1 = '''
        <div id="spannable">hello</div>
            <div id="tagcloud"></div>
            <div id="spannable"><a href="""">tag1</a></div>
        '''

    text2 = '<div id="spannable">12345678901234567890</div>'

    text3 = '<div id="spannable">hihihihi<div>45</div></div>'

    text4 = '<div><div id="spannable">123456789012345890</div></div>'

    text5 = '<div style="color:red" id="spannable" >12345678901234567890</div>'

    print(replace_divs(text1))
    print(replace_divs(text2))
    print(replace_divs(text3))
    print(replace_divs(text4))
    print(replace_divs(text5))