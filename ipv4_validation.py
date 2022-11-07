def solution(inputArray):
    x = False
    if inputArray.count('.') != 3:
        return x
    a=list(map(int, [i for i in inputString.split('.') if i != '' and not (i[0] == '0' and len(i) > 1) and i.isnumeric()]))
    if len(a) == 4:
        for b in a:
            if 0 <= b <= 255:
                x = True
            else:
                x = False
                break
    return x
if __name__ == '__main__':
    inputString = '0..1.0.0'
    
    print(solution(inputString))