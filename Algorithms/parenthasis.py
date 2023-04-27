def if_right_seq(seq: str) -> bool:
    pairs = {')': '(', '}': '{', ']': '[', '>':'<'}
    stack = []

    for i in range(len(seq)):
        elem = seq[i]

        if elem not in pairs:
            stack.append(elem)
        else:
            if not len(stack) or stack[-1] != pairs[elem]:
                return False
            else:
                stack.pop()

    return True


def find_end(seq: str, index: int) -> str:
    pairs = {')': '(', '}': '{', ']': '[', '>': '<'}
    stack = [seq[index]]

    for i in range(index + 1, len(seq)):
        elem = seq[i]

        if elem not in pairs:
            stack.append(elem)

        else:
            if stack[-1] == pairs[elem]:
                stack.pop()
                if not len(stack):
                    return seq[index: i + 1]
            else:
                return seq[index]


if __name__ == '__main__':
    strings = ['()()()()', '{}()[]<>', '{()[)}', '()(())(())[[]]{}{}{{}}', '(){}[]<>', '}[]()', '{}[]([])>']
    for s in strings:
        print(if_right_seq(s))

    print('-'*20)
    print(find_end('{[]()[]}', 0))
