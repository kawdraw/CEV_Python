contador = 0
soma = 0

while True:
    numero = int(input('Digite um valor [Digite 999 para parar]: '))
    if numero == 999:
        break
    contador += 1
    soma += numero


print(f'Você digitou {contador} vezes e a soma entre eles é {soma}')