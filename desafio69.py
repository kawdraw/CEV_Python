idade = 0
sexo = ''
contadorH = 0
contadorM = 0
contador = 0
while True:
    idade = int(input('Quantos anos a pessoa tem: '))
    sexo = input('Qual o sexo [H/M]: ').upper()
    if sexo != 'H' and sexo != 'M':
        print('Sexo invalido tente novamente com [H] para homen e [M] para mulher')
        continue
    proceguir = input('Você deseja continuar a coletar dados?[S/N]: ').upper()
    if proceguir != 'S':
        break
    if idade >=18:
        contador += 1
    if sexo == 'M' and idade <= 20:
        contadorM += 1
    if sexo == 'H':
        contadorH += 1

print(f'Foram cadastradas {contador} pessoas maiores de 18 anos\nForam cadastrados {contadorH} homens\nForam cadastradas {contadorM} mulhers menores de 20 anos')