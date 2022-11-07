'''Given a rectangular matrix containing only digits, calculate the number of different 2 X 2 squares in it.'''

from itertools import combinations
def solution(matrix):
    mos = []
    
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            k = 0
            sl1 = matrix[i][j:j+2]
            sl2 = matrix[i+1][j:j+2]
            c = [sl1, sl2]
            if c not in mos:
                mos.append(c)
        
    return len(mos)


if __name__ == '__main__':
    matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
    print(solution(matrix))