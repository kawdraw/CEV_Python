def leiaInt (text):
    indentificador = False
    valor = 0
    while True:
        num = input(text)
        if num.isnumeric():
            valor = int(text)
            indentificador = True
        else:
            print('\033[0;31mERRO digite um número inteiro\033[m')
        if indentificador == True:
            break
    return valor


num = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {num}')