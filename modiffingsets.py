n = int(input())
s = set(map(int, input().split()))
m = int(input())
val = 0
for i in range(m):
    l = input().split()
    if l[0] == 'pop':
        try:
            s.pop()
        except:
            pass
    elif l[0] == 'remove':
        try:
            s.remove(int(l[1]))
        except:
            pass
    else:
        s.discard(int(l[1]))
for j in s:
    val += j
print(val)