def fun(km,lt):
    gt = km/lt
    if gt < 8:
        print('Gasta muito!')
    elif gt > 8 and gt < 15:
        print('Econômico')
    elif gt>15:
        print('Super Econômico')

dt = float(input('Digite a distância em Km: '))
gs = float(input('Digite o consumo de gasolina em Litros: '))

fun(dt,gs)
           