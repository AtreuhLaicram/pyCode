def solution(a, b):
    x = False
    ad = [a[i] - b[i] for i in range(len(a)) if a[i] - b[i] != 0]
    if len(ad) <= 2:
        if len(ad) == 0:
            x = True
        else:
            if  sorted(a) == sorted(b):
                x = True
            else:
                x = False
    return x



if __name__ == '__main__':
    a = [1, 2, 2]
    b = [2, 1, 1]
    print(solution(a, b))