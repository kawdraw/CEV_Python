def QualOMaior (*num):
    maior = 0
    for c in (num):

        if c > maior:
            maior = c
        if len(num) == 0:
            print('Não foram adicionados números')

    print(f'Entre os números {num} o maior é {maior} e foram digitados {len(num)} números')
    maior -= maior

QualOMaior(9, 4, 7, 2, 3, 30)
QualOMaior(0, 2, 5, 50)
QualOMaior(4)
QualOMaior()