'''Dada una matriz de cadenas de igual longitud, se debe saber si es posible reorganizar el orden de los elementos de tal manera que cada par consecutivo de cadenas difiera exactamente en un carácter. Return true if it's possible, and false if not.'''
from itertools import permutations
def solution(inputArray):

    for i in permutations(inputArray):
        c = 0
        for j in range(len(i) - 1):
            for k in range(len(i[j])):
                if i[j][k] != i[j+1][k]:
                    c += 1
            if i[j] == i[j+1]:
                c += 2
        if c == len(i) - 1:
            return True
    return False

if __name__ == '__main__':
    a = ["abc", "abx", "axx", "abx", "abc"]
    print(solution(a))
    a = ["abc", "abx", "axx", "abc"]
    print(solution(a))