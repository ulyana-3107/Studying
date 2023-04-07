# Recursively determine if a list is a palindrome


def if_palindrome1(lst: list) -> bool:
    if len(lst) in range(2):
        return True
    elif lst[0] != lst[-1]:
        return False
    else:
        return if_palindrome1(lst[1:-1])


def if_palindrome2(lst: list, index=0) -> bool:
    if len(lst) == 2:
        if lst[0] == lst[-1]:
            return True
        return False
    elif len(lst) == 1:
        return True
    i1, i2 = index, -(index + 1)
    if i1 == len(lst)//2:
        if len(lst) % 2:
            return True
        return False
    if lst[i1] != lst[i2]:
        return False
    elif lst[i1] == lst[i2]:
        # 1) проверяем, не последние ли:
        if i1 == len(lst)//2 - 1 and i2 == -(len(lst)//2):
            return True
        else:
            return if_palindrome2(lst, index + 1)


test_cases = [[1, 2, 3, 4, 5], [1, 2, 3, 2, 1], [1, 2, 3, 3, 2, 1], [66, 77, 34, 33, 22]]
for test in test_cases:
    print(test, if_palindrome1(test), if_palindrome2(test),  sep='---')