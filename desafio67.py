resultado = 0

while True:
    numero = int(input('\nDigite um número que você queira ver a tabuada: '))
    if numero < 0:
        break
    for i in range (1, 11):
        resultado = numero*i
        print(f'{numero}x{i}={resultado}', end=' ')
print('Acabou')