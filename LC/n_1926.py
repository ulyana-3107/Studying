# from sortedcontainers import SortedDict # for another realisation (in process)
from collections import deque


def show_maze(maze:list, entrance) -> None:
    a, b = entrance
    maze[a][b] = 'S'
    print('\t\tMaze:')
    for m in maze:
        print(m)

def find_exits_ways(maze:list, entrance) -> tuple: # check if possible to speed up this function
    m, n, exits, moves = len(maze), len(maze[0]), set(), set()
    for i in range(m):
        for j in range(n):
            if i in (0, m - 1) or j in (0, n - 1):
                if maze[i][j] != '+' and [i, j] != entrance:
                    exit = (i, j)
                    exits.add(exit)
            if maze[i][j] == '.' and [i, j] != entrance:
                moves.add((i, j))
    return exits, moves

# def form_steps(entrance:list, moves:set) -> dict:
#     entrance_a, entrance_b = entrance
#     steps = dict()
#     for m in moves:
#         diff_a, diff_b = abs(m[0] - entrance_a), abs(m[1] - entrance_b)
#         steps[m] = diff_a + diff_b
#     return steps

def bfs_maze(entrance, moves, exits) -> tuple:
    visited, queue = {entrance}, deque([entrance])
    steps_num = 0
    while queue:
        curr = queue.popleft()
        if curr in exits:
            break
        else:
            i1, i2 = curr
            steps_num += 1
            neighbours = [(i1 + 1, i2), (i1 - 1, i2), (i1, i2 + 1), (i1, i2 - 1)]
            for n in neighbours:
                if n in moves:
                    queue.append(n)
    if curr != entrance:
        return curr,steps_num
    else:
        return None

def get_out_of_maze(maze:list, entrance:tuple) -> int:

    exits_moves = find_exits_ways(maze, entrance)
    exits, moves = exits_moves
    show_maze(maze, entrance)
    print(f'\nentrance: {entrance},\nexits: {exits}, \nmoves: {moves}\n')
    if not len(exits):
        return -1
    closest_exit = bfs_maze(tuple(entrance), moves, exits)
    print(f'closest exit: {closest_exit[0]}')
    if closest_exit:
        return f'Number of steps needed:{closest_exit[1]}'
    else:
        return -1

# mazes:
m_, e_ = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],
          ["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]], [0, 1]
m0, e0 = [[".","+","."]], [0, 2]
m1, e1 = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1, 2]
m2, e2 = [["+","+","+"],[".",".","."],["+","+","+"]], [1, 0]
m3, e3 = [[".","+"]], [0, 0] # 0
m4, e4 = [['+', '+', '+', '.', '+'], ['+', '+', '.', '+', '+'], ['.', '+', '.', '+', '+'], ['.' for i in range(5)],
          ['+', '+', '.', '+', '+']], [3, 1] # 1
m5, e5 = [['+', '+', '+', '.', '+', '+'], ['.', '+', '.', '.', '+', '.'], ['.', '+', '.', '.', '+', '+'],
          ['+', '.', '.', '+', '+', '.'], ['+', '+', '.', '.', '.', '.'], ['+' for i in range(6)]], [2, 2] # 3
m6, e6 = [['+' for _ in range(8)], ['.', '.', '+', '.','.','.','.','+'], ['+', '.','.','.','.','.','.','+'],
          ['+', '.','.','.','.','.','.','+'],['+', '.','.','.','.','.','.','+'],['+', '.','.','.','.','.','.','+'],
          ['+', '.','.','.','.','.','.','+'], ['+' for _ in range(8)]], [6, 6] # 11
m7, e7 = [['+' for _ in range(4)], ['+', '.', '.', '+'], ['+', '.', '.', '+'], ['+', '+', '.', '+']], [3, 2] # -1

tests = [(m_, e_), (m0, e0),(m1, e1), (m2, e2), (m3, e3), (m4, e4), (m5, e5), (m6, e6), (m7, e7)]
for t in tests:
    print(get_out_of_maze(t[0], t[1]), '\n'+'-' * 50)


# Plan:
# 1) find all the exits, add them to set, create SortedDict
# 2) find all the paths to that exits
# 3) return the first element of SortedDict

# def find_shortest_path(start:tuple, end:tuple) -> tuple:  # another realisation
#     pass

# steps_exit = SortedDict() # another realisation
    # for exit in exits:   # another realisation
    #     path_steps = find_shortest_path(entrance, exit)
    #     steps_exit[path_steps[1]] = exit
    # for s in steps_exit.keys():
    #     step = s
    #     break
    # return step

    #class Solution:
    # def find_exits_ways(maze:list, entrance) -> tuple: # check if possible to speed up this function
    #     m, n, exits, moves = len(maze), len(maze[0]), set(), set()
    #     for i in range(m):
    #         for j in range(n):
    #             if i in (0, m - 1, n - 1) or j in (0, m - 1, n - 1):
    #                 if maze[i][j] != '+' and [i, j] != entrance:
    #                     exit = (i, j)
    #                     exits.add(exit)
    #             if maze[i][j] == '.' and [i, j] != entrance:
    #                 moves.add((i, j))
    #     return exits, moves
    #
    # def form_steps(entrance:list, moves:set) -> dict:
    #     entrance_a, entrance_b = entrance
    #     steps = dict()
    #     for m in moves:
    #         diff_a, diff_b = abs(m[0] - entrance_a), abs(m[1] - entrance_b)
    #         steps[m] = diff_a + diff_b
    #     return steps
    #
    # def bfs_maze(entrance, moves, exits) -> tuple:
    #     visited, queue = {entrance}, deque([entrance])
    #     while queue:
    #         curr = queue.popleft()
    #         if curr in exits:
    #             break
    #         else:
    #             i1, i2 = curr
    #             neighbours = [(i1 + 1, i2), (i1 - 1, i2), (i1, i2 + 1), (i1, i2 - 1)]
    #             for n in neighbours:
    #                 if n in moves:
    #                     queue.append(n)
    #     if curr != entrance:
    #         return curr
    #     else:
    #         return None
    #
    # def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    #     exits_moves = find_exits_ways(maze, entrance)
    #     exits, moves = exits_moves
    #     show_maze(maze, entrance)
    #     if not len(exits):
    #         return -1
    #     steps, closest_exit = form_steps(entrance, moves), bfs_maze(tuple(entrance), moves, exits)
    #     if closest_exit:
    #         return steps[closest_exit]
    #     else:
    #         return -1