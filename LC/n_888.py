# Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where
# aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies
# of the jth box of candy that Bob has. Since they are friends, they would like to exchange one candy box each so that
# after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum
# of the number of candies in each box they have. Return an integer array answer where answer[0] is the number of
# candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange.
# If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.


# a, b = [1, 6, 3],  [3, 7, 4]
# a_, b_ = sum(a), sum(b)
# diff = abs(a_ - b_)
# print(diff)
 # Solution:
 # 1) мы находим разницу, а затем смотрим, у кого сумма больше
 # 2) эту разницу делим на два, и подбираем числа таким образом, чтобы разница между ними была равна той разнице, разде
 # ленной на два, и чтобы эта разница получалась посредством вычитания числа из массива с бОльшей суммой числа с мЕньшей
# суммой, как только такие числа найдены, они возвращаются
def box_exchange(a: list, b: list) -> list:
    s_a, s_b = sum(a), sum(b)
    # a, b = set(a), set(b)
    diff = abs(s_a - s_b)
    d2 = diff // 2
    if s_a > s_b:
        for i in b:
            j = d2 + i
            if j in a:
                return [j, i]
    else:
        for i in a:
            j = d2 + i
            if j in b:
                return [i, j]


a, b = [1, 1], [2, 2]  # [1, 2]
c, d = [1, 2], [2, 3]  # [1, 2]
e, f = [2], [1, 3]     # [2, 3]
print(box_exchange(e, f))