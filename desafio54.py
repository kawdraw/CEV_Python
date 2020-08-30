from datetime import date
anoAtual = date.today().year
listaAnos = []

for c in range (0,7):
    ano = int(input('Qual o ano que a pessoa nasceu? '))
    listaAnos.append(ano)

contMaiorDeIdade = 0
for ano in listaAnos:
    if anoAtual - ano >= 18: 
        contMaiorDeIdade += 1

print('A quantidade de maiores de idade é {}'.format(contMaiorDeIdade))
print('A quantidade de menores de idade é {}'.format(7 - contMaiorDeIdade))