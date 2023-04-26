# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most
# one cookie. Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content
# with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i
# will be content. Your goal is to maximize the number of your content children and output the maximum number.


def solution(g: list, s: list) -> int:
    # g.sort()
    # c = 0
    # for elem in s:
    #     c += elem
    # c2 = 0
    # for el in g:
    #     if c == 0:
    #         return c2
    #     elif c < 0:
    #         return c2 - 1
    #     c -= el
    #     c2 += 1
    # return c2
    g.sort()
    c2 = 0
    c = sum(s)
    for el in g:
        if c == 0:
            return c2
        elif c < 0:
            return c2 - 1
        c -= el
        c2 += 1


print(solution([1, 2, 3], [1, 1]))
