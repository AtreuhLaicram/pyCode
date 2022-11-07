'''Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.'''

def solution(n):
    centerValue = n*n
    vim = [i + 1 for i in range(centerValue)]
    matrix = [[0 for e in range(n)] for d in range(n)] # Creates the Matrix full of ceros
    cp = n // 2 # Center point of the matrix
    if n % 2 != 0:
        x = y = cp # The first coordinate, the starting point
        fx = False # Flag to determine if the next movement is to the left or to the right
        fy = True # Flag to determine if the next movement is up or down
    else:
        x = cp -1  # The first coordinate, the starting point
        y = cp
        fx = True # Flag to determine if the next movement is to the left or to the right
        fy = False # Flag to determine if the next movement is up or down
    
    dx = 1 # Distance to determine lenght or amount of movements for x
    dy = 1 # Distance to determine lenght or amount of movements for y
    ic = 0 # Steps counter
    pi = len(vim) - 1
    matrix[y][x] = centerValue # Sets the value at the center
    while 0 < pi and (0 <= x <= len(matrix[0]) and 0 <= y <= len(matrix)): # Main bucle to fill the matrix
        pi -= 1
        i = vim[pi] # Pointer to the next avalilable value to put on the matrix

        if fy and not fx: # The x goes to left
            ic += 1
            x -= 1
            if ic == dx:
                ic = 0
                dx += 1
                fx = True
        elif fx and fy: # the y goes down
            ic += 1
            y += 1
            if ic == dy:
                ic = 0
                dy += 1
                fy = False
        elif fx and not fy: # The y goes up
            ic += 1
            x += 1
            if ic == dy:
                ic = 0
                dx += 1
                fx = False
        elif not fx and not fy: # The x goes to right
            ic += 1
            y -= 1
            if ic == dy:
                ic = 0
                dy += 1
                fy = True
        matrix[y][x] = i

    return matrix


    


if __name__ == '__main__':

    n = 9
    a = solution(n)
    for x in a:
        print(x)
'''[[1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]'''    