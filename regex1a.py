import re


def find_links(text: str) -> list:
    pat = r'<a.*?(?:id=["\'].+?["\'])?.*?href=["\'](.+?)[\'"].*?(?:id=[\'"].+?[\'"])?.*?</a>'
    pat2 = r'href=["\'](.+?)["\']'
    return re.findall(pat2, text, flags=re.DOTALL)


text = '''
Blablablablablablabal
<a
 id="111w" href="Link1"></a>
<a id="22ee2" href="Link2"></a>
<a id="333" class="my_class" href="Link3"></a>
<a id="444" href='Link4'></a>
<a href="Link5" id="555">Some text</a>
blablabla'''

with open('html1a.txt', 'w', encoding='utf-8-sig') as input_file:
    input_file.write(text)

with open('html1a.txt', 'r', encoding='utf-8-sig') as input_reader2:
    text = ''
    for l in input_reader2.readlines():
        text += l
    links = find_links(text)

with open('links1a.txt', 'w', encoding='utf-8-sig') as writer:
    for l in links:
        writer.write(l + '\n')
