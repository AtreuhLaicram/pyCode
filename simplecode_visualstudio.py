from socket import gethostname


def simplecode():
    equipo = gethostname()
    print('Hola\nMe presento, soy {}, esta computadora.\n'.format(equipo))
    a = input('¿Cuál es tu nombre? >>: ')
    while a != 'x':
        b = input('Hola, {}. ¿Cómo te va el día de hoy? >>: '.format(a))
        if b != 'mal' or b != 'x':
            print('\nExcelente. Qué bueno que te está yendo {}\nEspero que encuentres esta sesión divertida'.format(b))
            print('He aquí un menú de opciones por hacer. Ingresa la opción deseada:\n')
            b2 = input('1. Navegar en Internet\n2. Editar un video o una foto\n3. Revisar tus archivos\n4. Salir del sistema\n>>: ')
            if b2 == '4':
                return
            elif b2 == '2':
                pass
            elif b2 == '3':
                pass
            elif b2 == '1':
                pass
            else:
                return
        elif b == 'x':
            return
        elif b == 'mal':
            print('Siento escucharlo. ¿Puedo asyudarte de alguna manera?\n')
            c = input('?')
            if c != 'no':
                d = input('De acuerdo. Dime cómo')
            else:
                e = input('Escribe x si quieres terminar la sesión')
                if e != 'x':
                    simplecode()
                else:
                    return
simplecode()
print('Sistema terminado!')