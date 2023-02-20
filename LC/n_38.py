class Solution:
    def countAndSay(self, n: int) -> str:
        dict = {'1': '1', '2': '11', '3': '21', '4': '1211', '5': '111221', '6': '312211', '7': '13112221',
                '8': '1113213211', '9': "31131211131221", '10': "13211311123113112211"}
        if n < 11:
            return dict[str(n)]
        else:
            line = str(n)
            l, arr, string = len(line), [], ''
            for i in range(l - 1):
                string += line[i]
                if line[i + 1] != line[i]:
                    arr.append(string)
                    string = ''
                if i == l - 2:
                    if len(string):
                        arr.append(string)
            print(f'arr: {arr}')
            last = arr[-1][-1]
            if line[-1] == last:
                arr[-1] += last
            else:
                arr += line[-1]
            result = ''
            for el in arr:
                a, b = el[0], str(len(el))
                add = b + a
                result += add
            return result
