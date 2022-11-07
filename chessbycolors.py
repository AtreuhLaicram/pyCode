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
	cl = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
	# Se ubica la posición de la celda en el tablero de ajedrez
	pos1 = ta[cl[cell1[0]]][int(cell1[1])]
	pos2 = ta[cl[cell2[0]]][int(cell2[1])]
	if pos1 == pos2: # Esto significa que ambas celdas apuntan a un mismo color
		return True
	else:
		return False

if __name__ == '__main__':
	cell1 = 'A1'
	cell2 = 'C3'
	print(solution(cell1, cell2))