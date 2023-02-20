import re


text = 'We arrive on 23/09/2023. So you are welcome after 24/12/2023'
sub_pat, new_pat = r'(\d\d)/(\d\d)/(\d{4})', r'\1.\2.\3'


def change_data(old: str, new: str, text: str) -> str:
    return re.sub(old, new, text)


print(re.sub(sub_pat, new_pat, text))
