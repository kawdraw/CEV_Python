verdade = True
sexo = ''
while(verdade):
    sexo = input('Sexo [F/M]: ').upper()
    if sexo in 'FM':
        verdade = False
    else:
        print('Sexo inválido!')
print('O sexo escolhido foi {}'.format(sexo))