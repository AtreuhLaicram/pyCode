def solution(deposit, rate, times_reinvertion, retiros_promedio):
    bpy = deposit
    while times_reinvertion >= 1:
        bpy = (bpy * (1 + rate/100))
        bpy -= retiros_promedio
        times_reinvertion -= 1
    return bpy

if __name__ == '__main__':
    while input('Cálculadora ganancia de reinversión. Por favor ingrese los soguientes datos.\nEscriba x para salir: ').lower() != 'x':
        print('')
        try:
            deposit = float(input('a) Depósito Inicial: '))
            rate = float(input('b) Tasa de Interés del Período: '))
            times_reinvertion = int(input('c) Veces de Reinversión: '))
            retiros_promedio = int(input('d) Retiros parciales promedio: '))
        except:
            print('Ingreso de datos incorrecto. Programa terminado')
            break
        print('El saldo final incluida la ganancia es de ${:.2f}'.format(solution(deposit, rate, times_reinvertion, retiros_promedio)))