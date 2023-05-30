import re


def need_replace(m) -> bool:
    answer = False
    if len(m[5]) < 21:
        answer = True

    return answer


def div_to_span(text: str) -> str:
    p = r'((<div)(.*?)(id=[\'"]spannable[\'"])(.*?>)((?:(?:<div.*?</div>)?.*))</(div)>)'
    sub_p = r'<span\3\4\5\6</span>'

    for obj in re.findall(p, text):
        if need_replace(obj):
            res = re.sub(p, sub_p, obj[0])
            text = text.replace(obj[0], res)

    return text


if __name__ == '__main__':

    text1 = '''
    <div id="spannable">hello</div>
        <div id="tagcloud"></div>
        <div id="spannable"><a href="""">tag1</a></div>
    '''

    text2 = '<div id="spannable">12345678901234567890</div>'

    text3 = '<div id="spannable">hihihihi<div>45</div></div>'

    text4 = '<div><span id="spannable">12345678901234567890</span></div>'

    text5 = '<div style="color:red" id="spannable">12345678901234567890</div>'

    print(div_to_span(text1))
    print(div_to_span(text2))
    print(div_to_span(text3))
    print(div_to_span(text4))
    print(div_to_span(text5))
