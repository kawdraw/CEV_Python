gols = []
jogador = dict()
time = list()

while True:
    jogador.clear()
    jogador['Nome'] = input('Qual o nome do jogador: ')
    jogos = int(input('Quantos jogos ele jogou: '))
    gols.clear()
    for j in range (0, jogos):
        gols.append(int(input(f'Quantos gols ele fez na {j}º partida: ')))

    jogador['Jogos'] = jogos
    jogador['Gols por Partida'] = gols
    tot = 0
    for g in gols:
        tot += g
    jogador['Total de Gols'] = tot
    time.append(jogador.copy())
    while True:
        porteiro = input('Você deseja continuar a passar informações de jogadores?[S/N] ').upper()
        if porteiro in 'SN':
            break
        print('ERRO responda somente com S ou N')
    if porteiro == 'N':
        break

while True:
    cod = int(input(f'Dados de qual jogador você quer visualizar [Por favor de 0 a {len(time) - 1}] 999 para parar: '))
    if cod > len(time):
        print(f'ERRO não tem nem um jogador cadastrado no número {cod}')
    if cod == 999:
        break
    else:
        print(f'Os dados do jogador {time[cod]["Nome"]}:\nEle participou de {time[cod]["Jogos"]} Partidas \nNessas partidas ele fez {time[cod]["Gols por Partida"]} Gols em cada partida \nO total de gols foi {time[cod]["Total de Gols"]}')
