lista = [[], [], []]

for i in range (0, 3):
    lista[0].insert(i, int(input(f'Digite um número para a casa 0,{i}: ')))
for i in range (0, 3):
    lista[1].insert(i, int(input(f'Digite um número para a casa 1,{i}: ')))
for i in range (0, 3):
    lista[2].insert(i, int(input(f'Digite um número para a casa 2,{i}: ')))
print(lista[0])
print(lista[1])
print(lista[2])