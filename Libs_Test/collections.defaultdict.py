from collections import defaultdict


word = 'missisipi'
d = defaultdict(int)

for w in word:
    d[w] += 1

print(sorted(d.items()))