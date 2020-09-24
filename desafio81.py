numeros = list()

while True:
    numero = int(input('Digite um valor numérico: '))
    numeros.append(numero)
    porteiro = input('Você deseja continuar digitando valores?[S/N] ').upper()
    if porteiro == 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números')
print(f'A sequencia de números decrecente é {numeros}')
if 5 in numeros:
    print('O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')