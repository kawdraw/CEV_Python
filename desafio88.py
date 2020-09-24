from random import randint

jogoDaMegaSena = list()
cont = 0
conta = 0
vezes = int(input('Quantos jogos você quer? '))

while conta != vezes:
    conta += 1
    while True:
        numero = randint(1, 60)
        if numero not in jogoDaMegaSena:
            jogoDaMegaSena.append(numero)
            cont += 1
        if cont >= 6:
            break
    jogoDaMegaSena.sort()
    print(jogoDaMegaSena)
    jogoDaMegaSena.clear()
    cont = 0