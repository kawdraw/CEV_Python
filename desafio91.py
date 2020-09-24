from random import randint
numeros = {}
deposito = {}

for c in range (1, 5):
    numeros[f'Jogador {c}º'] = (randint(1, 6))

print(numeros)
while True:

    if len(numeros) == 0:
        break
    maior = 0
    for j, n in numeros.items():
        if n > maior:
            maior = n
            jogador = j
    deposito[jogador] = maior
    del numeros[jogador]

print(deposito)