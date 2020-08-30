primeiroTermo = int(input('Digite o 1ª termo: '))
razao = int(input('Digite a razão: '))
cont, contadorPA = 10, 10

while cont > 0:
    print('{}'.format(primeiroTermo), end = ' => ')
    primeiroTermo += razao
    cont -= 1
    if cont == 0:
        print('PAUSA')
        cont = int(input('Você deseja continuar mais quantas vezes? '))
        contadorPA += cont

print('A quantidade total foi {}'.format(contadorPA + cont))