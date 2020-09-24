gols = []

jogador = dict()
jogador['Nome'] = input('Qual o nome do jogador: ')
jogos = int(input('Quantos jogos ele jogou: '))

for j in range (0, jogos):
    gols.append(int(input(f'Quantos gols ele fez na {j}º partida: ')))

jogador['Jogos'] = jogos
jogador['Gols por Partida'] = gols
tot = 0
for g in gols:
    tot += g
jogador['Total de Gols'] = tot
for k, v in jogador.items():
    print(f'{k} {v}')