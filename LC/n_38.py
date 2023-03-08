class Solution:
    def countAndSay(self, n: int) -> str:
        dict = {'1': '1', '2': '11', '3': '21', '4': '1211', '5': '111221', '6': '312211', '7': '13112221',
                '8': '1113213211', '9': "31131211131221", '10': "13211311123113112211"}
        if n < 11:  # O(1)
            return dict[str(n)]
        else:
            line = str(n)  # O(1)
            l, arr, string = len(line), [], ''  # O(1)
            for i in range(l - 1):  # L - количество цифр в числе  O(L)
                string += line[i]  # O(1)
                if line[i + 1] != line[i]:  # O(1)
                    arr.append(string)  # O(1)
                    string = ''  # O(1)
                if i == l - 2:  # O(1)
                    if len(string):  # O(1)
                        arr.append(string)  # O(1)
            last = arr[-1][-1]  # O(1)
            if line[-1] == last:  # O(1)
                arr[-1] += last  # O(1)
            else:
                arr += line[-1]
            result = ''
            for el in arr:  # O(L*2) -> O(L)
                a, b = el[0], str(len(el))
                add = b + a
                result += add
            return result
    # O(L) + O(L) -> O(L).
