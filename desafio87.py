lista = [[], [], []]
seEPar = 0
soma = 0
segundaLinha = 0
for i in range (0, 3):
    lista[0].insert(i, int(input(f'Digite um número para a casa 0,{i}: ')))
    if lista[0][i] % 2 == 0:
        seEPar += lista[0][i]
for i in range (0, 3):
    lista[1].insert(i, int(input(f'Digite um número para a casa 1,{i}: ')))
    if lista [1][i] > segundaLinha:
        segundaLinha = lista[1][i]
    if lista[1][i] % 2 == 0:
        seEPar += lista[1][i]
for i in range (0, 3):
    lista[2].insert(i, int(input(f'Digite um número para a casa 2,{i}: ')))
    if lista[2][i] % 2 == 0:
        seEPar += lista[2][i]
for i in range (0, 3):
    soma += lista[i][2]
print(lista[0])
print(lista[1])
print(lista[2])
print(f'A soma dos números pares foi {seEPar}')
print(f'O resultado da soma da terceira coluna {soma}')
print(f'O maior número da segunda linha é {segundaLinha}')