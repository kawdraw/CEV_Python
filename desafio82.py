numeros = list()
pares = list()
impares = list()

while True:
    numero = int(input('Digite um valor numérico: '))
    numeros.append(numero)
    porteiro = input('Você deseja continuar a adicionar valores?[S/N] ').upper()
    if porteiro == 'N':
        break
for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(numeros)
print(pares)
print(impares)