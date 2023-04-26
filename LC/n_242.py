# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.


def solution(s: str, t: str) -> bool:
     all, s, t = set((s + t).lower()), s.lower(), t.lower()
     alp_code,  c = {}, 0
     for elem in all:
          alp_code[elem] = c
          c += 1
     s1, t1 = [alp_code[i] for i in s], [alp_code[i] for i in t]
     if len(s1) > 2:
          for i in range(len(s1)):
               m = s1[i], i
               for j in range(i + 1, len(s1)):
                    if s1[j] < m[0]:
                         m = s1[j], j
               if s1[i] > m[0]:
                    s1[i], s1[m[1]] = s1[m[1]], s1[i]
     if len(t1) > 2:
          for i in range(len(t1)):
               m = t1[i], i
               for j in range(i + 1, len(t1)):
                    if t1[j] < m[0]:
                         m = t1[j], j
               if t1[i] > m[0]:
                    t1[i], t1[m[1]] = t1[m[1]], t1[i]
     return t1 == s1


print(solution('hello', 'olehl'))