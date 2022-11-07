'''Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku'''

def solution(grid):
    for m in range(0, len(grid)-3, 3):        
        for n in range(0, len(grid[m])-3, 3):
            q = grid[m][n:n+3] + grid[m+1][n:n+3] + grid[m+2][n:n+3]
            w = set(q)
            if len(w) != 9:
                return False
    for i in grid:
        u = set(i)
        if len(u) != 9:
            return False
        u = set()
    for k in range(len(grid[0])):
        co = []
        for j in range(len(grid)):
            co.append(grid[j][k])
        v = set(co)
        if len(v) != 9:
            return False
        v = set()

    return True
if __name__ == '__main__':

    grid = [[1,3,2,5,4,6,9,8,7], 
            [4,6,5,8,7,9,3,2,1], 
            [7,9,8,2,1,3,6,5,4], 
            [9,2,1,4,3,5,8,7,6], 
            [3,5,4,7,6,8,2,1,9], 
            [6,8,7,1,9,2,5,4,3], 
            [5,7,6,9,8,1,4,3,2], 
            [2,4,3,6,5,7,1,9,8], 
            [8,1,9,3,2,4,7,6,5]]
    print(solution(grid))   