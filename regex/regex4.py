import re


def div_span(text: str) -> str:

    p = r'((<div)(.*?)id=[\'"]spannable[\'"](.*?>)(.{,20})</div>)'
    sub_pat = r'<span\3\4\5</span>'

    return re.sub(p, sub_pat, text)


if __name__ == '__main__':

    text1 = '''
    <div id="spannable">hello</div>
        <div id="tagcloud"></div>
        <div id="spannable"><a href="""">tag1</a></div>
    '''

    text2 = '<div id="spannable">12345678901234567890</div>'