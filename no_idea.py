m, n = map(int, input().split())
x = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happy_factor = 0

for i in x:
    if i in a:
        happy_factor +=1
    elif i in b:
        happy_factor -= 1
print(happy_factor)