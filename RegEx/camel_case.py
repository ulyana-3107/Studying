import re
# underdone

text = '''MyVar17 = OtherVar + YetAnother2Var 
TheAnswerToLifeTheUniverseAndEverything = 42'''


def camel_to_underscore(text: str) -> str:
    print(re.findall('r(?<=[A-Z][a-z]+)\s', text))


camel_to_underscore(text)

# import re
#
#
# text = '''MyVar17 = OtherVar + YetAnother2Var
# TheAnswerToLifeTheUniverseAndEverything = 42'''
#
#
# # task: Владимир написал свой открытый проект, именуя переменные в стиле «ВерблюжийРегистр».
# # И только после того, как написал о нём статью, он узнал, что в питоне для имён переменных принято использовать
# # подчёркивания для разделения слов (under_score). Нужно срочно всё исправить, пока его не «закидали тапками».
# # Задача могла бы оказаться достаточно сложной, но, к счастью, Владимир совсем не использовал строковых констант и
# # классов. Поэтому любая последовательность букв и цифр, внутри которой есть заглавные, — это имя переменной, которое
# # нужно поправить.
#
# def count_len(lst: list) -> int:
#     c = 0
#     for l in lst:
#         c += len(l)
#     return c
#
#
# def camel_case_edit(text: str) -> str:
#     pat1 = ''
#     pat2 = ''
#     return re.sub(pat1, pat2, text)
#
#
# p = r'(([A-Z])([a-z0-9]+))'
#
#
# borders = [[i.start(), i.end()] for i in re.finditer(p, text)]
# print(borders)
# new_borders, length = [], 0
# while length != len(borders):
#     sub = []
#     for i in range(length, len(borders)):
#         if not len(sub):
#             sub.append(borders[i])
#             if i == len(borders):
#                 new_borders.append(sub)
#         else:
#             if borders[i][0] == sub[-1][-1]:
#                 sub.append(borders[i])
#             else:
#                 new_borders.append(sub)
#                 length = count_len(new_borders)
#                 break
#         if i == len(borders) and count_len(new_borders) != len(borders):
#             new_borders.append(sub)
#     length = count_len(new_borders)
#
# print(new_borders