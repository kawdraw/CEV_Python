qtdCedula50 = 0
qtdCedula20 = 0
qtdCedula10 = 0
qtdCedula1 = 0

while True:
    saque = int(input('Qual o valor a ser sacado: '))
    qtdCedula50 = saque // 50
    resto = saque % 50
    if qtdCedula50 != 0:
        print(f'{qtdCedula50} notas de R$ 50,00')
    qtdCedula20 = resto // 20
    resto = resto % 20
    if qtdCedula20 != 0:
        print(f'{qtdCedula20} notas de R$ 20,00')
    qtdCedula10 = resto // 10
    resto = resto % 10
    if qtdCedula10 != 0:
        print(f'{qtdCedula10} notas de R$ 10,00')
    qtdCedula1 = resto // 1
    resto = resto % 1
    if qtdCedula1 != 0:
        print(f'{qtdCedula1} notas de R$ 1,00')
    if resto == 0:
        break
