from datetime import datetime


def vota (anoDeNascimento):
    idade = datetime.now().year - anoDeNascimento
    if idade > 16 < 18 or idade > 65:
        print(f'Com a idade de {idade} o voto é facultativo')
    elif idade < 16:
        print(f'Com a idade de {idade} não é possível votar')
    else:
        print(f'Com a idade de {idade} o voto é obrigatorio')


vota(int(input('Que ano você nasceu?: ')))