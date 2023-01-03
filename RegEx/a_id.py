import re


text = '…<a id="1234">Some text</a>…98/76/5432…<a id="1234">Some text</a>…98/76/5432…'
text_ = '<a class="b_hide" Id="111" href="" h="ID=SERP,5493.1">Random_text</a>'
text_0 = '<a class="b_hide" id="P334" href="" h="ID=SERP,5493.1"></a>'
text_1 = '<a class="b_hide" ID="00088" h="ID=SERP,5495"></a>'


for i in (text, text_, text_0, text_1):
    res = re.search(r'(?:<a\s.*[idID]=["](\d+)["].*[>](.*)[<]/a>)', i)
    if res:
        print(res[1], '-', res[2])



