def solution(deposit, rate, time_ci):
    a = deposit*(1+(rate/100))**time_ci
    return a

if __name__ == '__main__':
    print('Cálculadora ganancia de reinversión. Por favor ingrese los soguientes datos.')
    deposit = float(input('a) Depósito Inicial: '))
    rate = float(input('b) Tasa de Interés del Período: '))
    time_ci = int(input('c) Veces de Reinversión: '))
    print('El saldo final incluida la ganancia es de ${:.2f}'.format(solution(deposit, rate, time_ci)))