from collections import deque
# Алгоритм:
# 1. если каждый человек знает не больше 1го - ответ Yes.
# 2. выбираем человека с максимальным количеством знакомых и помещаем его в группу номер 1
# 3. берем всех его знакомых и помещаем их в группу номер 2
# 4. проходимся по людям из второй группы: создаем список всех знакомых тут, затем:
# если его нет в первой группе, проверяем нет ли там общих знакомых, если нет - добавляем, если есть - ответ No.
# 5. в порядке убывания по количеству знакомых проходимся по всем остальным, проделывая те же шаги.


def create_data(matrix: list) -> tuple:
    friends, friends_num, n = {}, {}, len(matrix)
    for i in range(n):
        friends[i] = set()
        for j in range(n):
            if matrix[i][j] and i != j:
                friends[i].add(j)
        friends_num[i] = len(friends[i])
    return friends, friends_num


def friends_true(s: set, friends: dict) -> bool:
    for elem in s:
        if len(friends[elem]&s):
            return True
    return False


def dividible(matrix: list):
    distributed, gr1, gr2 = set(), set(), set()
    friends, friends_num = create_data(matrix)
    sorted_friends_num = {}
    sorted_d = sorted(friends_num, key=friends_num.get)
    sorted_d.reverse()
    if sorted_d[0] < 2:
        return 'Yes'
    for elem in sorted_d:
        if elem not in distributed and not len(gr1):
            distributed.add(elem)
            gr1.add(elem)
            friends_ = friends[elem]
            gr2 = gr2.union(friends_)
            if friends_true(gr2, friends):
                return 'No', None, None
            distributed = distributed.union(gr2)
            friends_2 = []
            for elem in gr2:
                friends_2.extend(list(friends[elem]))
            for f in friends_2:
                if f not in gr1:
                    if not len(gr1 & friends[f]):
                        gr1.add(f)
                        distributed.add(f)
                    else:
                        return 'No', None, None
        elif elem not in distributed:
            if not len(gr1 & friends[elem]):
                gr1.add(elem)
                distributed.add(elem)
            elif not len(gr2 & friends[elem]):
                gr2.add(elem)
                distributed.add(elem)
    gr1, gr2 = [i + 1 for i in list(gr1)], [i + 1 for i in list(gr2)]
    return 'Yes', gr1, gr2

# matrix = [
#           [1, 0, 0, 0, 0, 1],
#           [0, 1, 0, 1, 0, 0],
#           [0, 0, 1, 0, 1, 0],
#           [0, 1, 0, 1, 1, 0],
#           [0, 0, 1, 1, 1, 0],
#           [1, 0, 0, 0, 0, 1]  # Yes
#          ]
# matrix = [[0, 1, 0, 0, 0],
#           [1, 0, 0, 0, 0],
#           [0, 0, 0, 1, 1],
#           [0, 0, 1, 0, 1],
#           [0, 0, 1, 1, 0]]  # No
# matrix = [[1, 0, 0, 1, 1],
#           [0, 1, 0, 1, 1],
#           [0, 0, 1, 1, 1],
#           [1, 1, 1, 1, 0],
#           [1, 1, 1, 0, 1]]  # Yes
# matrix = [[1, 0, 1, 0, 0],
#           [0, 1, 0, 0, 1],
#           [1, 0, 1, 0, 0],
#           [0, 0, 0, 1, 1],
#           [0, 1, 0, 1, 0]]  # Yes


matrix = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]  # Yes
with open('friends_matrix.txt', 'w', encoding = 'utf-8-sig') as writer:
    for line in matrix:
        writer.write(' '.join([str(i) for i in line]) + '\n')

with open('friends_matrix.txt', 'r', encoding='utf-8-sig') as reader:
    m = []
    for line in reader.readlines():
        m.append([int(i) for i in line.strip().split(' ')])

result = dividible(m)

with open('friends_result.txt', 'w', encoding='utf-8-sig') as writer:
    if type(result) == str:
        writer.write(result)
    else:
        for elem in result:
            writer.write(str(elem) + '\n')