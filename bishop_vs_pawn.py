'''Determina si dos celdas dada son blancas o negras o de diferente color, en un tablero de ajedrez'''
def solution(cell1, cell2):

    # Tablero de ajedrez
    ta = []

    for filas in range(8):
        fyc = []
        if filas % 2 == 0:
            for cols in range(8):
                if cols % 2 == 0:
                    fyc.append(1)
                else:
                    fyc.append(0)
        else:
            for cols in range(8):
                if cols % 2 == 0:
                    fyc.append(0)
                else:
                    fyc.append(1)
        ta.append(fyc)
    # Diccionario para nombres de celda
    cl = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    # Se ubica la posición de la celda en el tablero de ajedrez
    pos1 = ta[cl[cell1[0]]][int(cell1[1])-1]
    pos2 = ta[cl[cell2[0]]][int(cell2[1])-1]
    if pos1 == pos2: # Esto significa que ambas celdas apuntan al mismo color
        if abs(cl[cell1[0]] - cl[cell2[0]]) == abs(int(cell1[1]) - int(cell2[1])):
            return True        
    return False

if __name__ == '__main__':
	bishop = 'h1'
	pawn = 'a8'
	print(solution(bishop, pawn))