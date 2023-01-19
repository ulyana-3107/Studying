from collections import deque


class Solutions(object):

    def min_mutation(self, start_gene: str, end_gene: str, bank: list) -> int:
        queue, seen = deque([(start_gene, 0)]), {start_gene}  # o(1)

        while queue:  # if len(bank) is B -> O(B)
            gene, steps = queue.popleft()  # O(1)
            if gene == end_gene:  # O(1)
                return steps
            for l in 'ACGT':  # O(4) -> O(1)
                for i in range(len(gene)):  # O(8) -> O(1)
                    neib = gene[: i] + l + gene[i + 1:]  # O(len(gene)) == O(1), -> O(1)
                    if neib in bank and neib not in seen:  # O(1)
                        queue.append((neib, steps + 1))  # O(1)
                        seen.add(neib)  # O(1)

        return -1
# O(1) + O(B) * (O(1) + O(1) + o(1)) -> O(B)


s1, e1, b1 = 'AACCGGTT', 'AACCGGTA', ['AACCGGTA']
s2, e2, b2 = 'AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']
tests = [s1, e1, b1, s2, e2, b2]
i = 0
while i < len(tests):
    start, end, bank = tests[i], tests[i + 1], tests[i + 2]
    obj = Solutions()
    print(obj.min_mutation(start, end, bank))
    i += 3

