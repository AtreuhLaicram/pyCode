def solution(inputString):
    x = True
    ldl = [a for a in inputString]
    ldl.sort()
    e = len(ldl)%2
    for b in range(1, len(ldl)):
        if ldl[b] == ldl[b-1]:
            ldl.append(ldl[b])
            ldl.pop(b)
        else:
            ldl.append(ldl[b-1])
            ldl.pop(b-1)
    if e == 0 and not ldl[0].isnumeric():
        c = ldl[:len(ldl)//2]
        d = sorted(ldl[len(ldl)//2:])
        if c == d:
            x=True
        else:
            x=False
    else:
        c = ldl[:len(ldl)//2]
        d = sorted(ldl[1+len(ldl)//2:])
        if c == d:
            x=True
        else:
            x=False
    return x

if __name__ == '__main__':
    inputString = "caab1bc"
    print(solution(inputString))