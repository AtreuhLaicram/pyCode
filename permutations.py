from itertools import permutations

s, l = input().split()
k = int(l)
listap = []
if 0 < k <= len(s):
    for tupla in list(permutations(s,k)):
        v = ''
        for l in tupla:
            v += l
        listap.append(v.upper())
        listap.sort()
    print("\n".join(listap))
            
        