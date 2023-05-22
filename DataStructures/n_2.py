from __future__ import annotations


def find_right_sequence(seq: str) -> str|int|tuple:
    stack = []
    pairs = {']': '[', '}': '{', ')': '('}
    for i in range(len(seq)):
        elem = seq[i]
        if elem not in pairs:
            stack.append(elem)
        else:
            if stack[-1] == pairs[elem]:
                stack.pop()
            else:
                return seq[: i]
    if not len(stack):
        return 'Correct', seq
    return len(stack)


sequences = ['(())', '()', '[({})]', '(([[]]})', '[{]}']
for seq in sequences:
    print(f'{seq} : {find_right_sequence(seq)}')