import re


def links_finder(text: str) -> list:
    pat = r'(?<=href=)"{1,}([^"]+)(?=")'
    return re.findall(pat, text)


t = '''
<a
 id=""111"" href=""Link1""></a>
<a id=""222"" href=""Link2""></a>
<a id=""333"" class=""my_class"" href=""Link3""></a>
<a id=""444"" href='Link4'></a>
<a href=""Link5"" id=""555"">Some text</a>
blablabla
'''


print(links_finder(t))


