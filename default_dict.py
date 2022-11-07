from collections import defaultdict

n, m = map(int, input().split())
groupa = defaultdict(list)
groupb = defaultdict(list)

for wa in range(n):
    groupa[wa].append(input())
for wb in range(m):
    groupb[wb].append(input())
for indx, mth in groupb.items():
    reslist = []
    for index, nth in groupa.items():
        if mth == nth:
            reslist.append(index + 1)
    if len(reslist) > 0:
        print(" ".join(map(str, reslist)))
    else:
        print(-1)