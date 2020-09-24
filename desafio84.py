dados = list()
pessoas = list()
contador = 0
maiorPeso = 0
menorPeso = 99999
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    porteiro = input('Você deseja continuar a adicionar dados?[S/N] ').upper()
    contador += 1
    if porteiro != 'S':
        break

for pessoa in pessoas:
    peso = pessoa[1]
    nome = pessoa[0]
    if peso >= maiorPeso:
        maiorPeso = peso

    if peso <= menorPeso:
        menorPeso = peso


print(f'Foram adicionado os dados de {contador} pessoas')

print(f'Maior pesso foi {maiorPeso}', end=' ')
for i in pessoas:
    if i[1] == maiorPeso:
        print(f'{i[0]}', end=' ')
print(f'\nMenor pesso foi {menorPeso}', end=' ')
for i in pessoas:
    if i[1] == menorPeso:
        print(f'{i[0]}', end=' ')