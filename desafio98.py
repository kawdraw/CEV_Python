from time import sleep


def contador (inicio, fim, passo):
    if passo == 0:
        passo += 1
    if fim < inicio:
        passo = -passo

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for c in range(inicio, fim, passo):
        print(f'{c}',end=' ')
    print('')
    print('-='*30)



contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de fazer uma contagem personalizada')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)