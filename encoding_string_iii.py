'''Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters'''


def solution(s):
    ltr = [] # División de subcadenas de letras iguales
    h = 0 # Indice inicial de la división de s
    i = 1 # Indice final de la divisuón de s
    if len(s) >= 2: # Sólo si la cadena tiene más de un caracter
        while i < len(s):
            while i < len(s) and s[h] == s[i]: # Mientras la letra a la que apunta st es igual a la siguiente...
                i += 1 # Incrementa el apuntador final y compara de nuevo
            ltr.append(s[h:i]) # Alimenta la lista de subcadenas cuando detecta diferencia
            h = i # Incrementa el contador inicial al siguiente caracer posible
    else: # Si la cadena es de un caracter, se devuelve igual
        return s
    n = [str(len(f))+f[0] for f in ltr] # Lista de las letras de las divisiones de s
    for x in range(len(n)): # Elimina los unos del conteo de letras
        if n[x][0] == '1' and n[x][1].isalpha():
            n[x] = n[x][1]

    return "".join(n) # Devuelve la línea codificada

    return "".join(n)
        

if __name__ == '__main__':
    s = "aaabbac"
    print(solution(s))