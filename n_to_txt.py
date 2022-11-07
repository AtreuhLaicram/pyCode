def numtotext(number):
    los=[]
    dic_unidades={1:"uno", 2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",0:"cero"}
    dic_unidadesdediez={1:"once",2:"doce",3:"trece",4:"catorce",5:"quince",6:"dieci"}
    dic_decenas={1:"veinte",2:"veinti",3:"treinta",4:"cuatenta",5:"cincuenta",6:"sesenta",7:"setenta",8:"ochenta",9:"noventa"}
    dic_centenas={1:"ciento", 2:"cientos",5:"quinientos",7:"setecientos",9:"novecientos",0:""}
    dic_miles={1:"mil"}
    ''' dic_millones={1:"millón",2:"millones"}
    dic_billones={1:"billón",2:"billones"}'''
    num_pos=[int(n) for n in number]
    num_pos.reverse()
    print(num_pos)
    for pos in range(len(num_pos)):
        if pos==0:
            los.append(dic_unidades[num_pos[pos]])
        if pos==1:
            if  num_pos[pos]==1:
                los.append(dic_unidadesdediez[num_pos[pos]])
            else:
                los.append(dic_decenas[num_pos[pos]])
        if pos==2:
            los.append(dic_centenas[num_pos[pos]])
        if pos==3:
            los.append(dic_miles[1])
        if pos==4:
            los.append(dic_unidades[num_pos[pos]])
        if pos==5:
            if  num_pos[pos]==1:
               los.append(dic_unidadesdediez[num_pos[pos]])
            else:
                los.append(dic_unidades[num_pos[pos]])
        if pos==6:
            los.append(dic_centenas[num_pos[pos]])
        if pos==7:
            los.append(dic_miles[1])
        if pos==8:
            los.append(dic_unidades[num_pos[pos]])
        if pos==10:
            if  num_pos[pos]==1:
                los.append(dic_unidadesdediez[num_pos[pos]])
            else:
                los.append(dic_decenas[num_pos[pos]])
        if pos==11:
            los.append(dic_centenas[num_pos[pos]])
    los.reverse()
    return " ".join(los)
    
number=input()
print(numtotext(number))