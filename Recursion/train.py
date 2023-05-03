def if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps):
    index = i1 + i2
    if seq == res:
        return True
    if index == 0 and len(wrong_steps) and len(wrong_steps[0]) > 1:
        return False

    elem = res[index]

    if i1 >= len(l1) or i2 >= len(l2):
        if i1 >= len(l1):
            if seq + l2[i2:] == res:
                return True
            elif l2[i2] == elem:
                seq.append(l2[i2])
                steps.append(2)
                i2 += 1
                return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)
            else:
                s = steps.copy()
                wrong_steps.append(s)
                seq.pop()
                i1 -= 1
                steps.pop()
                return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)

        else:
            if seq + l1[i1:] == res:
                return True
            elif l1[i1] == elem:
                seq.append(l1[i1])
                steps.append(1)
                i1 += 1
                return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)
            else:
                s = steps.copy()
                wrong_steps.append(s)
                seq.pop()
                i2 -= 1
                steps.pop()
                return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)

    if l1[i1] == elem or l2[i2] == elem:
        if l1[i1] == elem and steps + [1] not in wrong_steps:
            seq.append(l1[i1])
            i1 += 1
            steps.append(1)
            return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)
        elif l2[i2] == elem and steps + [2] not in wrong_steps:
            seq.append(l2[i2])
            i2 += 1
            steps.append(2)
            return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)

        else:
            s = steps.copy()
            wrong_steps.append(s)
            l_step = steps.pop()
            if l_step == 1:
                i1 -= 1
            else:
                i2 -= 1
            seq.pop()
            return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)

    else:
        s = steps.copy()
        wrong_steps.append(s)
        l_st = steps.pop()
        seq.pop()
        if l_st == 1:
            i1 -= 1
        else:
            i2 -= 1
        return if_possible2(l1, l2, i1, i2, res, seq, steps, wrong_steps)


if __name__ == '__main__':

    l1_1, l2_1, res_1 = [1, 4, 3], [2, 4, 0], [1, 2, 4, 0, 4, 3]  # True
    l1_2, l2_2, res_2 = [1, 2, 1, 3], [1, 4, 2, 1], [1, 1, 2, 4, 2, 1, 3, 1]  # True
    l1_3, l2_3, res_3 = [1, 2, 1, 3], [1, 4, 2, 1], [1, 1, 1, 2, 1, 2, 3, 4]  # False
    l1_4, l2_4, res_4 = [1, 2, 2, 4, 8], [0, 2, 2, 3, 2], [1, 2, 0, 2, 4, 8, 2, 2, 3, 2]  # True
    l1_5, l2_5, res_5 = [0, 0, 2, 3, 6], [0, 1, 1, 3, 3], [0, 1, 0, 1, 0, 2, 3, 6, 3]  # True
    l1_6, l2_6, res_6 = [0, 1, 4, 4, 8], [0, 2, 3, 4, 6], [0, 0, 1, 2, 3, 4, 4, 6, 4, 8]  # True
    l1_7, l2_7, res_7 = [0, 1, 4, 4, 8], [0, 2, 3, 4, 6], [0, 0, 1, 2, 3, 4, 8, 4, 4, 6]  # False

    for i in range(1, 8):
        print(if_possible2(eval('l1_'+str(i)), eval('l2_'+str(i)), 0, 0, eval('res_'+str(i)), [], [], []))
