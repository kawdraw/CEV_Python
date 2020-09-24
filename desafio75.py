tupla = ()
pares = ()

for c in range (1,5):
    primeiro = int(input(f'Digite o {c}° número: '))
    tupla += (primeiro,)
    if primeiro % 2 == 0:
        pares += (primeiro,)

print(f'O numero 9 apareceu {tupla.count(9)} vezes.')

if tupla.count(3) >= 1:
    print(f'O número 3 apareceu a primeira vez na posição {tupla.index(3) + 1}.')
else:
    print('O número 3 não aparece nem uma vez.')

print(f'Os números pares são: {pares}')
