def notas (*num, situacao=False):
    """ A função notas
        notas (*num, situacao=False).
        num recebe todos os parametros de notas nesseçarios.
        situacao é uma ação opsional ativavel usando True no lugar de False.
        a função notas pega todos as notas, separa a maior e a menor nota e faz a média delas. """
    menor = 10
    maior = 0
    soma = 0
    for c in num:
        soma += c
        if c < menor:
            menor = c
        if c > maior:
            maior = c
    media = soma / len(num)
    print(f'As notas foram: {num}. \n{maior} foi a maior nota. \n{menor} foi a menor nota. \nE a média da turma foi {media}')
    if situacao == True:
        if media < 6:
            print('Situação Ruim')
        elif media > 6 and media < 8:
            print('Situação Rasoavel')
        else:
            print('Situação Boa')



notas(6.5, 5.2, 3.2, 4.5, 10, 8.5, situacao=True)
help(notas)