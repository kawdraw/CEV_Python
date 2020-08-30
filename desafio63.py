quantidade = int(input('Quantos termos você quer? '))
primeiro = 0
segundo = 1
resultado = primeiro + segundo
print('{} => {} => '.format(primeiro, segundo),end='')
while quantidade >= 3:
    print('{} => '.format(resultado),end = '')
    primeiro = segundo
    segundo = resultado
    resultado = primeiro + segundo
    quantidade -= 1
print('Fim')
