from random import randint
contadorDeVitorias = 0
carcteresCabecalho = '-=-'
print(f'{carcteresCabecalho * 10}')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(f'{carcteresCabecalho * 10}')

while True:
    numeroPc = randint(0, 10)
    print(numeroPc)
    parImpar = input('Par ou Ímpar? [P/I]: ').upper()

    if (parImpar not in 'PI') or (parImpar == 'PI'):
        print('\033[1m\033[91m**CARACTER INVÁLIDO!**\033[0m \nPor favor digite [P] para par ou [I] para ímpar')
        continue

    numeroJogador = int(input('Qual o seu número? '))
    soma = numeroJogador + numeroPc
    ehPar = soma % 2 == 0
    escolheuPar = parImpar == 'P'
    jogadorPerdeu = (ehPar and not escolheuPar) or (not ehPar and escolheuPar)

    if jogadorPerdeu:
        print(f'Você perdeu o resultado foi: {soma}')
        break

    contadorDeVitorias += 1
    print(f'Parabéns você ganhou, o resultado foi: {soma}')

print(f'Quantidade de VITÓRIAS: {contadorDeVitorias}')