'''Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.'''

def solution(product):
    sn = []
    y = product
    if y == 1:
        return 1
    if y == 0:
        return 10
    while y > 1:
        for x in range(9, 1, -1):
            if y % x == 0:
                y //= x
                sn.append(x)
                break
        else:
            return -1
    
    return int("".join(list(map(str, sorted(sn)))))

if __name__ == '__main__':
    product = 243
    print(solution(product))