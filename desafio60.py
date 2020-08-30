num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = ''
valor = 1

for i in range (num, 0, -1):
    if i > 1:
        fatorial = fatorial + '{} x '.format(i)
    else:
        fatorial = fatorial + '{} = '.format(i)
    valor *= i

print(fatorial + str(valor))