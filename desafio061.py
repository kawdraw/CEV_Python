primeiroTermo = int(input('Digite o 1ª termo: '))
razao = int(input('Digite a razão: '))
quantidade = int(input('Quantas vezes vc quer fazer essa PA? '))

while quantidade > 0:
    print('{}'.format(primeiroTermo), end = ' => ')
    primeiroTermo += razao
    quantidade -= 1

print('Fim')