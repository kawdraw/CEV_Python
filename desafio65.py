contador = 0
soma = 0
verificador = 'S'
maior = 0
menor = 100

while verificador != 'N':
    numero = int(input('Digite um número: '))
    verificador = str(input('Você deseja continuar [S/N]')).upper()
    contador += 1
    soma += numero
    media = soma / contador
    if numero >= maior:
        maior = numero
    if numero <= menor:
        menor = numero
print('Você mostrou {} números\nSoma entre eles é {}\nMédia é {}\nMaior número foi {}\nMenor foi {}'.format(contador, soma, media, maior, menor))