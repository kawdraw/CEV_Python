valores = list()
confirmar = ''
while confirmar != 'N':
    recebimentoDeValores = int(input('Digite um valor numérico: '))
    if recebimentoDeValores != valores:
        valores.append(recebimentoDeValores)
    confirmar = input('Você deseja continuar a digitar valores?[S/N]: ').upper()
valores.sort()
print(valores)