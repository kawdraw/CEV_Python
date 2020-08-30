sexoMasculino = 'm'
sexoFeminino = 'f'
mulherMenos20 = 0
somaIdades = 0
maiorIdade = 0
nomeDoVelho = ''

for i in range (1, 5):
    nome = input('Qual o nome da {}ª pessoa? '.format(i))
    idade = int(input('Qual a idade da {}ª pessoa?  '.format(i)))
    sexo = input('Qual o sexo da {}ª pessoa?(Responda com f de feminino ou m de masculino) '.format(i))
    somaIdades = somaIdades + idade

    if sexo == sexoMasculino and idade >= maiorIdade:
        maiorIdade = idade
        nomeDoVelho = nome

    if sexo == sexoFeminino and idade < 20:
        mulherMenos20 += 1

print('A média das idades é {}'.format(somaIdades / 4))
print('A quantidade de mulhers menores de vinte anos é {}'.format(mulherMenos20))
print('O nome do homem mais velho é {}'.format(nomeDoVelho))