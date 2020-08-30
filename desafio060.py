num = int(input('Digite um número para fazer seu cálculo fatorial: '))
fatorial = ''
valor = 1
c = num

while c > 0:
    if c > 1:
        fatorial += '{} x '.format(c)
    else:
        fatorial += '{} ='.format(c)
    valor *= c
    c -= 1

print('{} {}'.format(fatorial, valor))
