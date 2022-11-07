'''You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.'''
from itertools import combinations
s, k = input().split()
for j in range(1, int(k)+1):
    t = combinations(sorted(s),j)
    for x in t:
        o = ''
        for r in range(len(x)):
            o += x[r]
        print(o)