def numeroatexto(numero):
    nuevacadena = ""
    if numero == "0":
        return "cero"
    # Diccionarios para nombrar números dependiendo de la posición
    unidades = {
        "0":"",
        "1":"uno",
        "2":"dos",
        "3":"tres",
        "4":"cuatro",
        "5":"cinco",
        "6":"seis",
        "7":"siete",
        "8":"ocho",
        "9":"nueve"
    }
    decenas = {
        "0":"",
        "1":"diez",
        "2":"veinte",
        "3":"treinta",
        "4":"cuarenta",
        "5":"cincuenta",
        "6":"sesenta",
        "7":"setenta",
        "8":"ochenta",
        "9":"noventa"
    }
    centenas = {
        "0":"",
        "1":"cien",
        "2":"doscientos",
        "3":"trescientos",
        "4":"cuatrocientos",
        "5":"quinientos",
        "6":"seiscientos",
        "7":"setecientos",
        "8":"ochocientos",
        "9":"novecientos"
    }
    millares = {
        "0":"",
        "1":"mil",
        "2":"dos mil",
        "3":"tres mil",
        "4":"cuatro mil",
        "5":"cinco mil",
        "6":"seis mil",
        "7":"siete mil",
        "8":"ocho mil",
        "9":"nueve mil"
    }
    millones = {
        "0":"",
        "1":"un millón",
        "2":"dos millones",
        "3":"tres millones",
        "4":"cuatro millones",
        "5":"cinco millones",
        "6":"seis millones",
        "7":"siete millones",
        "8":"ocho millones",
        "9":"nueve millones"
    }
    billones = {
        "0":"",
        "1":"un billón",
        "2":"dos billones",
        "3":"tres billones",
        "4":"cuatro billones",
        "5":"cinco billones",
        "6":"seis billones",
        "7":"siete billones",
        "8":"ocho billones",
        "9":"nueve billones"
    }
    # Calcula la posición de un dígito
    lnumero = []
    lnumeroconvert = []
    i = 0
    for digito in numero:
        lnumero.insert(0, digito)
    #lnumero.reverse()
    j = 0
    for j in range(len(lnumero)):
        if j == 0:
            lnumeroconvert.insert(0, unidades[lnumero[j]]) 
        elif j == 1:
            lnumeroconvert.insert(0, decenas[lnumero[j]])
            if lnumeroconvert[0] == "veinte" and lnumeroconvert[1] != "":
                lnumeroconvert[0] = "veinti"
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "uno":
                lnumeroconvert[0] = "once"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "dos":
                lnumeroconvert[0] = "doce"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "tres":
                lnumeroconvert[0] = "trece"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "cuatro":
                lnumeroconvert[0] = "catorce"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "cinco":
                lnumeroconvert[0] = "quince"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] != "":
                lnumeroconvert[0] = "diceci"
            elif lnumeroconvert[1] != "":
                lnumeroconvert.insert(1, "y")
        elif j == 2:
            lnumeroconvert.insert(0, centenas[lnumero[j]])
            if lnumeroconvert[0] == "cien" and (lnumeroconvert[1] != "" or lnumeroconvert[2] != ""):
                lnumeroconvert[0] = "ciento"                
        elif j == 3:
            lnumeroconvert.insert(0, millares[lnumero[j]])
        elif j == 4:
            lnumeroconvert.insert(0, decenas[lnumero[j]])
            if lnumeroconvert[0] == "veinte" and lnumeroconvert[1] != "":
                lnumeroconvert[0] = "veinti"
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "uno":
                lnumeroconvert[0] = "once"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "dos":
                lnumeroconvert[0] = "doce"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "tres":
                lnumeroconvert[0] = "trece"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "cuatro":
                lnumeroconvert[0] = "catorce"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "cinco":
                lnumeroconvert[0] = "quince"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] != "":
                lnumeroconvert[0] = "diceci"
            elif lnumeroconvert[1] != "":
                lnumeroconvert.insert(1, "y")
        elif j == 5:
            lnumeroconvert.insert(0, centenas[lnumero[j]])
            if lnumeroconvert[0] == "cien" and (lnumeroconvert[1] != "" or lnumeroconvert[2] != ""):
                lnumeroconvert[0] = "ciento"
        elif j == 6:
            lnumeroconvert.insert(0, millones[lnumero[j]])
        elif j == 7:
            lnumeroconvert.insert(0, decenas[lnumero[j]])
            if lnumeroconvert[0] == "veinte" and lnumeroconvert[1] != "":
                lnumeroconvert[0] = "veinti"
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "uno":
                lnumeroconvert[0] = "once"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "dos":
                lnumeroconvert[0] = "doce"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "tres":
                lnumeroconvert[0] = "trece"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "cuatro":
                lnumeroconvert[0] = "catorce"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] == "cinco":
                lnumeroconvert[0] = "quince"
                lnumeroconvert[1] = ""
            elif lnumeroconvert[0] == "diez" and lnumeroconvert[1] != "":
                lnumeroconvert[0] = "diceci"
            elif lnumeroconvert[1] != "":
                lnumeroconvert.insert(1, "y")
        elif j == 8:
            lnumeroconvert.insert(0, centenas[lnumero[j]])
            if lnumeroconvert[0] == "cien" and (lnumeroconvert[1] != "" or lnumeroconvert[2] != ""):
                lnumeroconvert[0] = "ciento"
        elif j == 9:
            lnumeroconvert.insert(0, millares[lnumero[j]])
     
    nuevacadena = " ".join(lnumeroconvert)
    return nuevacadena

a = ""
while a.lower() != "x":
    a = input("Escriba un número a convertir a texto o escriba 'x' para terminar: ")
    if a.isnumeric():
        print("El número {} en texto es {}".format(a, numeroatexto(a)))
#    c = input("Presione Enter para continuar o escriba 'x' para terminar: ")