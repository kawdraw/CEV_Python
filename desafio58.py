from random import randrange
numeroRandomico = randrange(0, 10)
verificacao = True
cont = 0

while (verificacao):
    tentativa = int(input(f'Tente adivinhar um numero de 0 a 10: '))
    if numeroRandomico == tentativa:
        verificacao = False
    elif numeroRandomico > tentativa:
        print('Tente um número maior que {}'.format(tentativa))
    else:
        print('Tente um numero menor que {}'.format(tentativa))
    cont += 1

print('Parabéns, você acertou com {} tentativas. \nO número adivinhado foi {}'.format(cont, tentativa))