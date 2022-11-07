def solution(inputString):
    x = True
    r=0
    ldl = set([a for a in inputString])
    for m in ldl:
        r += inputString.count(m)%2
    if r <= 1:
        return True
    else:
        return False
    
if __name__ == '__main__':
    inputString = "caab1bc"
    print(solution(inputString))