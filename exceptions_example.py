t = int(input())
for test in range(t):
    try:
        a, b = input().split()
        print(a // b)
    except ZeroDivisionError or ValueError or KeyError or TypeError as e:
        print("Error Code:", e)