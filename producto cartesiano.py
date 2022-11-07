from itertools import product
a = input().split()
b = input().split()
v = ""
a1 = [int(h) for h in a]
b1 = [int(i) for i in b]
s = list(product(a1, b1))
for t in s:
    v += str(t) + " "
print(v.rstrip())
    