from random import randint

numeros = list()
numerosOrdenados = list()


for c in range (1, 6):
    numero = int(input('Digite um valor numérico: '))
    numeros.append(numero)

while True:
    menor = 10
    if len(numeros) == 0:
        break

    for numero in numeros:
        if numero < menor:
            menor = numero

    numeros.remove(menor)
    numerosOrdenados.append(menor)

print(numerosOrdenados)
