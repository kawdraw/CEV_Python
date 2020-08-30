soma = 0
numerosDeEntrada = 1
quantidade = 0

while numerosDeEntrada != 999:
    numerosDeEntrada = int(input('Digite um número [Para parar digite 999]: '))
    quantidade += 1
    soma = soma + numerosDeEntrada

print('A quantidade de números digitado foi {}, e o resultado da soma entre eles foi {}'.format(quantidade, soma - 999))