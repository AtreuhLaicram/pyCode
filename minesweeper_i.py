def solution(matrix):
    mweeper = [[0 for o in range(len(matrix[0])+2)] for wh in range(len(matrix)+2)]
    for i in range(len(matrix)):
        a = i + 1
        for k in range(len(matrix[0])):
            b = k + 1
            if matrix[i][k]:
                mweeper[a-1][b-1] += 1
                mweeper[a-1][b] += 1
                mweeper[a-1][b+1] += 1
                mweeper[a][b-1] += 1
                mweeper[a][b+1] += 1
                mweeper[a+1][b-1] += 1
                mweeper[a+1][b] += 1
                mweeper[a+1][b+1] += 1
    nmw=[r[1:-1] for r in mweeper[1:-1]]
    return nmw

if __name__ == '__main__':
    matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

    print(solution(matrix))
'''mweepr = [[1, 2, 1],
            [2, 1, 1],
            [1, 1, 1]]'''