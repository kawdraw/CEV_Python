primeiroTermo = int(input('Digite o 1ª termo: '))
razao = int(input('Digite a razão: '))

cont = 10

while cont > 0:
    print('{}'.format(primeiroTermo), end = ' => ')
    primeiroTermo += razao
    cont -= 1

print('Fim')
