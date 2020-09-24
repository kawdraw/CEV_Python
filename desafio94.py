galera = list()
pessoas = dict()
mulheres = list()
idadeAcimaDaMedia = list()
idade = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = input('Nome: ')
    while True:
        pessoas['Sexo'] = input('Sexo [F/M]: ').upper()
        if pessoas['Sexo'] in 'FM':
            break
        print('Erro F ou M sómente por favor tente novamente')
    pessoas['Idade'] = int(input('Idade'))
    idade += pessoas['Idade']
    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas.copy())
    galera.append(pessoas.copy())
    while True:
        resposta = input('Quer continuar a adicionar dados de pessoas?[S/N]: ').upper()
        if resposta in 'SN':
            break
        print('Erro digite S ou N, por favor tente novamente')
    if resposta == 'N':
        break

media = idade / len(galera)
for c in galera:
    if c['Idade'] > media:
        idadeAcimaDaMedia.append(c)

print(f'A quantidade de pessoas é {len(galera)}')
print(f'A média de idades {media}')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'A idade acima da media foi {idadeAcimaDaMedia}')