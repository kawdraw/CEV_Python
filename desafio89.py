lista = list()
while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resposta = input('Voce deseja continuar a adicionar dados? [S/N] ').upper()
    if resposta == 'N':
        break
for i, e in enumerate(lista):
    print(f'{i} {e[0]} {e[2]}')
while True:
    operador = int(input('Você quer a nota de qual aluno? (999 encerra) '))
    if operador == 999:
        print('Encerrando')
        break
    if operador <= len(lista):
        print(f'As notas do {lista[operador][0]} são {lista[operador][1]}')