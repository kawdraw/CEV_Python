from random import randrange
inicioRand = randrange(0, 10000000)
fimRand = randrange(10000001, 999999999999999999)
numeroRandomico = randrange(inicioRand, fimRand)
verificacao = True
cont = 1

while (verificacao):
    print(f'Tente adivinhar um numero de {inicioRand} a {fimRand}: ')
    tentativa = randrange(inicioRand, fimRand)

    if numeroRandomico == tentativa:
        verificacao = False
    elif numeroRandomico > tentativa:
        inicioRand = tentativa
        print('Tente um número maior que {}'.format(tentativa))
    else:
        fimRand = tentativa
        print('Tente um numero menor que {}'.format(tentativa))
    cont += 1

print('Parabéns, você acertou com {} tentativas. \nO número adivinhado foi {}'.format(cont, tentativa))