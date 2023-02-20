from collections import deque


class Solution:
    def nearestExit(self, maze, entrance) -> int:
        rows, cols = len(maze), len(maze[0])  # O(1)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))  # O(1)

        start_row, start_col = entrance  # O(1)
        maze[start_row][start_col] = "+"  # O(1)

        queue = deque()  # O(1)
        queue.append([start_row, start_col, 0])  # O(1)

        while queue:  # O(M*N) - the worst case where M, N - size of a matrix.
            curr_row, curr_col, curr_distance = queue.popleft()  # O(1)

            for d in dirs:  # O(4) -> O(1)
                next_row = curr_row + d[0]  # O(1)
                next_col = curr_col + d[1]  # O(1)

                if 0 <= next_row < rows and 0 <= next_col < cols \
                        and maze[next_row][next_col] == ".":  # O(1)

                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:  # O(1)
                        return curr_distance + 1  # O(1)

                    maze[next_row][next_col] = "+"  # O(1)
                    queue.append([next_row, next_col, curr_distance + 1])  # O(1)
        return -1
# 6 - 13: O(1)
# 16 - 29: O(1)
# 6 - 30: O(1) + O(M*N) * O(1) -> O(M*N).


# assume that 1 - wall, 0 - empty cell, 2 - entrance
def first_approach(maze: list, entrance: list = None):  # R - number of rows, C - number of columns
    len1, len2 = len(maze), len(maze[0])
    # first we iterate through maze indexes and form a list of possible steps
    steps, queue = [], deque([entrance + [0]])
    for i in range(len(maze)):  # O(R)
        for j in range(len(maze[i])):  # O(C)
            if maze[i][j] == 0 and [i, j] != entrance:
                steps.append([i, j])
    while queue:  # it depends on the number of empty cells and answer(less -> while loop ends fast, more -> otherwise)
        # O(?)
        i, j, d = queue.popleft()
        if i in (0, len1 - 1) and [i, j] != entrance or j in (0, len2 - 1) and [i, j] != entrance:
            return d
        else:
            neighbours = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            for n in neighbours:
                if n in steps:
                    queue.append(n + [d + 1])
    return -1
#  O(R*C) + O(?)


maze, entrance = [[0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]], [2, 0]
maze1, entrance1 = [[1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0],
                    [1, 0, 1, 0, 1, 1]], [5, 3]
# print(first_approach(maze1, entrance1))


def show_maze(maze, entrance) -> None:
    maze[entrance[0]][entrance[1]] = 'S'
    print('\t\tMaze:')
    for m in maze:  # O(len(maze)) -> if R - number of rows -> O(R)
        print(m)


def second_approach(maze, entrance) -> int:
    show_maze(maze, entrance)  # O(R)
    rows, cols = len(maze), len(maze[0])
    s_row, s_col = entrance
    maze[s_row][s_col] = '+'
    queue = deque()
    queue.append([s_row, s_col, 0])
    dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:  # O(R * C)
        curr_row, curr_col, curr_dist = queue.popleft()
        for d in dist:
            next_row, next_col = curr_row + d[0], curr_col + d[1]
            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '.':
                if next_row in (0, rows - 1) or next_col in (0, cols - 1):
                    return curr_dist + 1
                maze[next_row][next_col] = '+'
                queue.append((next_row, next_col, curr_dist + 1))
    return -1
# O(R * C)


m_, e_ = [["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+", ".", "+", ".", "+"],
          ["+", ".", ".", ".", "+", ".", "+"], ["+", "+", "+", "+", "+", ".", "+"]], (0, 1)
m0, e0 = [[".", "+", "."]], (0, 2)
m1, e1 = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], (1, 2)
m2, e2 = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], (1, 0)
m3, e3 = [[".", "+"]], (0, 0)  # 0
m4, e4 = [['+', '+', '+', '.', '+'], ['+', '+', '.', '+', '+'], ['.', '+', '.', '+', '+'], ['.' for i in range(5)],
          ['+', '+', '.', '+', '+']], (3, 1)  # 1
m5, e5 = [['+', '+', '+', '.', '+', '+'], ['.', '+', '.', '.', '+', '.'], ['.', '+', '.', '.', '+', '+'],
          ['+', '.', '.', '+', '+', '.'], ['+', '+', '.', '.', '.', '.'], ['+' for i in range(6)]], (2, 2)  # 3
m6, e6 = [['+' for _ in range(8)], ['.', '.', '+', '.', '.', '.', '.', '+'], ['+', '.', '.', '.', '.', '.', '.', '+'],
          ['+', '.', '.', '.', '.', '.', '.', '+'], ['+', '.', '.', '.', '.', '.', '.', '+'], ['+', '.', '.', '.', '.',
                                                                                               '.', '.', '+'],
          ['+', '.', '.', '.', '.', '.', '.', '+'], ['+' for _ in range(8)]], (6, 6)  # 11
m7, e7 = [['+' for _ in range(4)], ['+', '.', '.', '+'], ['+', '.', '.', '+'], ['+', '+', '.', '+']], (3, 2)  # -1

tests = [(m_, e_), (m0, e0), (m1, e1), (m2, e2), (m3, e3), (m4, e4), (m5, e5), (m6, e6), (m7, e7)]


# for t in tests:
#     l = len(t[0][0])
#     print(find_exit(t[0], t[1]))
#     print('~' * 40)
    # print(first_approach(t[0], t[1]), '\n'+'-' * 50)