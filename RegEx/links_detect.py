import re


def links_finder(file_link: str) -> list:
    pattern = r"<a .* href=\"(.+)\">"
    result_list = list()
    with open(file_link, 'r', encoding='utf-8-sig') as file:
        for line in file.readlines():
            result = re.findall(pattern, line)
            if len(result):
                result_list.extend(result)
    return result_list


link = input('Link:')
links_found = links_finder(link)
for link in links_found:
    print(link)

