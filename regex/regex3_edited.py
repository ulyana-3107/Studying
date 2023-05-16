# Дан html-файл. Удалить все теги <div>, внутри них нет тега <span>.
import re


def remove_divs_without_spans(line: str) -> str:
    parts = re.split(r"(<\s*div(?:>|(?:\s[^>]*>)))|(<\s*/div\s*>)", line)
    print('p:', parts)
    stack = [["", parts[0]]]
    for i in range(1, len(parts), 3):
        if parts[i]:
            stack.append([parts[i], parts[i+2]])
        else:
            div_def, div_cont = stack.pop()
            if re.search(f"<\s*span[\s>]", div_cont):
                stack[-1][-1] += div_def + div_cont + parts[i+1]
            stack[-1][-1] += parts[i+2]
    return stack[0][-1]


# print(remove_divs_without_spans("Test1 <div> Test2 <div id='spannable'> Test3 <span></span> Test4 </div> Test5 </div> Test6"))
# print(remove_divs_without_spans("Test1 <div> Test2 <div id='spannable'> Test3 Test4 </div> Test5 </div> Test6"))
# print(remove_divs_without_spans("Test1 <div   > Test2 <div   id='spannable'> Test3 <   span   ><  /span> Test4 <  /div   > Test5 <  /div  > Test6"))
# print(remove_divs_without_spans("Test1 <div   > Test2 <div   id='spannable'> Test3 Test4 <  /div   > <   span   ><  /span> Test5 <  /div  > Test6"))
# print(remove_divs_without_spans("Test1 <div   > <   span   ><  /span>  Test2 <div   id='spannable'> Test3 Test4 <  /div   > Test5 <  /div  > Test6"))
# print(remove_divs_without_spans(" Test0 <   span   ><  /span> Test1 <div   >  Test2 <div   id='spannable'> Test3 Test4 <  /div   > Test5 <  /div  > Test6"))
# print(remove_divs_without_spans(" Test0 Test1 <div   >  Test2 <div   id='spannable'> Test3 Test4 <  /div   > Test5 <  /div  > Test6 <   span   ><  /span> Test7"))
