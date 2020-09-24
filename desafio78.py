lista = list()
maior = 0
menor = 10
posicaoMaior = list()
posicaoMenor = list()

for c in range (1,6):
    valor = int(input(f'digite o {c}° número: '))
    lista.append(valor)
    if valor > maior:
        maior = valor
        posicaoMaior = [c]
    elif maior == valor:
        posicaoMaior.append(c)
    if valor < menor:
        menor = valor
        posicaoMenor = [c]
    elif menor == valor:
        posicaoMenor.append(c)
print(lista)
print(f'O maior número foi {maior} e ele aparece nas posições {posicaoMaior}\nO menor número foi {menor} que aparece nas posições {posicaoMenor}')