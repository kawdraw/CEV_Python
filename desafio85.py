numero = [[], []]

for c in range (0, 7):
    test = int(input('Digite um número: '))
    if test % 2 == 0:
        numero[0].append(test)
    else:
        numero[1].append(test)
numero[0].sort()
numero[1].sort()
print(numero)