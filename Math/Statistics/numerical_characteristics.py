from collections import defaultdict


def method(selection: list) -> dict:
    d = {}
    m, w = defaultdict(int), dict()
    # nums_set = set(selection)
    for num in selection:
        m[num] += 1
    n = sum(m.values())
    for k, v in m.items():
        w[k] = round(v/n, 2)
    sa_mean = sum(selection)/n
    xi_mi, xi_wi = [round(x*m, 2) for x, m in m.items()], [round(x*w, 2) for x, w in w.items()]
    sa_weighted_1 = round(sum(xi_wi), 2)
    sa_weighted_2 = round(sum(xi_mi)/n, 2)
    print(f'1:{sa_weighted_1}, 2:{sa_weighted_2}')





sel = [40, 43, 43, 46, 46, 46, 54, 56, 59, 62, 64, 64, 66, 66, 67, 67, 68, 68, 69, 69, 69, 71, 75, 75, 76, 76, 78, 80,
       82, 82, 82, 82, 82, 83, 84, 86, 88, 90, 90, 91, 91, 92, 95, 102, 127]
method(sel)
