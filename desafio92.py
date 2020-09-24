from datetime import datetime
info = {}
info ['Nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
info ['Idade'] = datetime.now().year - ano
info ['Carteira'] = int(input('Número da Carteira de trabalho (se não tem = 0): '))
if info ['Carteira'] != 0:
    info ['Contratação'] = int(input('Ano de contratação: '))
    info ['Salário'] = float(input('Qual o valor do Salário: '))
    info ['Aposentadoria'] = info ['Idade'] + ((info ['Contratação'] + 35) - datetime.now().year)
print(info)