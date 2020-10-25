def ficha (nome='', gols=0):
    if nome == '':
        print('Jogador desconhecido',end=' ')
    else:
        print(f'O jogador: {nome}',end=' ')
    if gols == '':
        print('Fez 0 gols no campeonato')
    else:
        print(f'Fez {gols} gols no campeonato')


nome = input('Qual o nome do jogador: ')
gols = input('Quantos gols ele fez: ')
ficha(nome, gols)