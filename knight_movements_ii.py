'''Given a position of a k on the standard chessboard, find the number of different moves the k can perform.'''


def solution(cell):
    # Diccionario para nombres de celda
    cl = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    filaInicial = cl[cell[0]]
    columnaInicial = int(cell[1])-1
    mov_posible = 0
    k1u2r = [filaInicial + 1, columnaInicial + 2]
    k2u1r = [filaInicial + 2, columnaInicial + 1]
    k2u1l = [filaInicial + 2, columnaInicial - 1]
    k1u2l = [filaInicial + 1, columnaInicial - 2]
    k1d2r = [filaInicial - 1, columnaInicial + 2]
    k2d1r = [filaInicial - 2, columnaInicial + 1]
    k2d1l = [filaInicial - 2, columnaInicial - 1]
    k1d2l = [filaInicial - 1, columnaInicial - 2]

    if 0 <= k1u2r[0] <=7 and 0 <= k1u2r[1] <=7:
        mov_posible += 1
    if 0 <= k2u1r[0] <=7 and 0 <= k2u1r[1] <=7:
        mov_posible += 1
    if 0 <= k2u1l[0] <=7 and 0 <= k2u1l[1] <=7:
        mov_posible += 1
    if 0 <= k1u2l[0] <=7 and 0 <= k1u2l[1] <=7:
        mov_posible += 1
    if 0 <= k1d2r[0] <=7 and 0 <= k1d2r[1] <=7:
        mov_posible += 1
    if 0 <= k2d1r[0] <=7 and 0 <= k2d1r[1] <=7:
        mov_posible += 1
    if 0 <= k2d1l[0] <=7 and 0 <= k2d1l[1] <=7:
        mov_posible += 1
    if 0 <= k1d2l[0] <=7 and 0 <= k1d2l[1] <=7:
        mov_posible += 1
    
    return mov_posible
        

if __name__ == '__main__':
    cell = "h8"
    print(solution(cell))