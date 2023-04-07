import re
# underdone


# task: На вход даётся номер телефона, как его мог бы ввести человек. Необходимо его переформатировать в формат
# +7 123 456-78-90. Если с номером что-то не так, то нужно вывести строчку Fail!.


text = '''+7 123 456-78-90, 8(123)456-78-90, 7(123) 456-78-90, 1234567890, 123456789, +9 123 456-78-90,+7 123 456+78=90,
+7(123 45678-90, 8(123  456-78-90'''


def format_number(number: str) -> str:
    digits = re.findall(r'\d', number)
    if len(digits) < 10:
        return 'Fail'
    elif len(digits) == 10:
        pass
    else:
        if int(digits[0]) not in (7, 8):
            return 'Fail'
        else:
            string = ''.join(digits)
            pat = r'(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)'
            sub_pat = r'+\1 \2\3\4 \5\6\7-\8\9-\10\11'
            print('replaced:', re.sub(pat, sub_pat, string))


nums = text.split(',')
for num in nums:
    print(f'num: {num}')
    format_number(num)


def replace(num: str) -> str:
    pat = r'([+]?([7-8]?)([\(\s]{,2})(\d{3})([\)\s]{,2})(\d{3})([-]?)(\d{2})([-]?)(\d{2}))'
    sub_pat = r'+7 \4 \6-\8-\10'
    if re.search(pat, num):
        if num[1] != '9' and num[0] != '9':
            return re.sub(pat, sub_pat, num)
        return 'Fail'
    return 'Fail'


nums = ['+7 123 456-78-90', '8(123)456-78-90', '7(123) 456-78-90', '1234567890', '123456789', '+9 123 456-78-90',
        '+7 123 456+78=90', '+7(123 45678-90', '8(123  456-78-90']
answers = ['+7 123 456-78-90', '+7 123 456-78-90', '+7 123 456-78-90', '+7 123 456-78-90', 'Fail!', 'Fail!', 'Fail!',
           '+7 123 456-78-90', 'Fail!']


for num in nums:
    print(f'num: {num},    result: {replace(num)}'+'\n')


