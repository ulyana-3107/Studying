def road_building(n, edges) -> str:  # N, E - n, len(edges)
    addr, components, comp_num = {i: i for i in range(1, n + 1)}, {i: [i] for i in range(1, n + 1)}, ''  # O(N)
    for e in edges:  # O(E)
        town_a, town_b = e  # O(1)
        town_a_addr, town_b_addr = addr[town_a], addr[town_b]  # O(1)
        if town_a_addr == town_b_addr:  # O(1)
            comp_num += str(n) + ' '  # O(1)
        else:
            size_a, size_b = len(components[town_a_addr]), len(components[town_b_addr])  # O(1)
            a, b = size_a >= size_b, size_b > size_a  # O(1)
            if a:  # O(1)
                saved_towns = components[town_b_addr]  # O(1)
                components[town_a_addr].extend(saved_towns)  # O(len(saved_towns)) -> O(N - 1) -> O(N)
                for s_t in saved_towns:  # O(N)
                    addr[s_t] = town_a_addr  # O(1)
                components[town_b_addr] = []  # O(1)
            else:
                saved_towns = components[town_a_addr]   # O(1)
                components[town_b_addr].extend(saved_towns)  # O(len(saved_towns)) -> O(N - 1) -> O(N)
                for s_t in saved_towns:  # O(N)
                    addr[s_t] = town_b_addr  # O(1)
                components[town_a_addr] = []  # O(1)
            if n > 1:  # O(1)
                n -= 1  # O(1)
            comp_num += str(n) + ' '  # O(1)
    return comp_num

# 4 - 5:  O(1)
# 12 - 16: O(1) + O(N) + O(N)*O(1) + O(1) -> O(N)
# 18 - 22: O(1) + O(N) + O(N)*O(1) + O(1) -> O(N)
# 9 - 25: O(1) + O(1) + max(O(N), O(N)) + O(1) + O(1) + O(1) -> O(N)
# 6 - 25: O(1) + max(O(1), O(N)) -> O(1) + O(N) -> O(N)
# 3 - 26: O(E) * O(N) -> O(N*E)
# RESULT: O(NE)

# n, q, edges = 4, 3, [(1, 2), (3, 4), (2, 3)]  # 3 2 1
# n, q, edges = 7, 6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]  # 6 5 4 3 2 2
# n, q, edges = 6, 6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]  # 5 4 3 2 1 1
# n, q, edges = 6, 5, [[1, 4], [5, 2], [1, 3], [5, 4], [6, 2]]  # 5 4 3 2 1
# n, q, edges = 5, 5, [[1, 2], [3, 4], [1, 3], [3, 5], [1, 5]]  # 4 3 2 1 1
# n, q, edges = 8, 7, [[1, 8], [7, 2], [3, 6], [4, 5], [5, 3], [6, 2], [1, 7]]  # 7 6 5 4 3 2 1
# n, q, edges = 8, 6, [[1, 5], [5, 6], [3, 4], [1, 2], [7, 8], [2, 3]]  # 7 6 5 4 3 2
# n, q, edges = 7, 6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]  # 6 5 4 3 2 2
# n, q, edges = 9, 6, [[7, 3], [2, 9], [4, 8], [5, 6], [9, 8], [5, 7]]  # 8 7 6 5 4 3
# n, q, edges = 8, 9, [[2, 7], [7, 8], [3, 2], [4, 1], [8, 2], [1, 8], [1, 7], [3, 4], [3, 5]]  # 7 6 5 4 4 3 3 3 2


n_, q_, edges_ = 9, 8, [(2, 7), (6, 9), (2, 6), (3, 7), (3, 6), (9, 4), (5, 1), (8, 4)]  # '8 7 6 5 5 4 3 2'

with open('road_build_input.txt', 'w', encoding='utf-8-sig') as input_writer:
    input_writer.write(str(n_) + ' ' + str(q_) + '\n')
    for e_ in edges_:
        input_writer.write(str(e_[0]) + ' ' + str(e_[1]) + '\n')
    print('Input is written.')

with open('road_build_input.txt', 'r', encoding='utf-8-sig') as input_reader:
    edges_, n_ = [], int(input_reader.readline().strip().split(' ')[0])
    for line in input_reader.readlines():
        edges_.append([int(i) for i in line.strip().split(' ')])
    print('Input is read.')

components_number = road_building(n_, edges_)
print('Output is ready.')

with open('road_build_output.txt', 'w', encoding='utf-8-sig') as output_writer:
    output_writer.write(components_number)
    print('Output is written')