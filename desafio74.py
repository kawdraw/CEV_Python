from random import randint
maior = 0
menor = 10

listaDeNumeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for c in listaDeNumeros:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'{listaDeNumeros} \nMaior número{maior}\nMenor número{menor}')