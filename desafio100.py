from random import randint
numeros = []
def sorteia (Random):
    for c in range (0, 5):
        numeros.append(randint(0, 50))
    print(f'Os números sorteados foram {numeros}')
def somaPar (soma):
    par = 0
    for c in numeros:
        if c % 2 == 0:
            par += c
    print(f'A soma dos números pares foi {par}')


sorteia(1)
somaPar(1)