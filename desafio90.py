aluno = {}

aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input('Média: '))
if aluno['Média'] > 7:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'

for c, v in aluno.items():
    print(f'{c} do aluno, {v}')