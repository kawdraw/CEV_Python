def fatorial (x=1, show = False):
    """ fatorial (x, show = False):
        Aonde se encontra o X é aonde você coloca um valor para fazer o seu fatorial.
        Se você colocar um valor no X e não mudar o show para True você só vai obter o resultado da fatorial
        Agora se você mudar o show para True você vai ter como resultado o calcúlo da fatorial e seu resultado"""
    num = list()
    f = 1

    for c in range (x, 0, -1):
        f *= c
        num.append(c)

    if x <= 0:
        f = 0
        num.append(0)
    if show:
        print(f'O cálculo do fatorial de {x} é:')
        print(*num, sep="*", end=' = ')
        print(f)
    else:
        print(f'O resultado do fatorial {f}')



fatorial(int(input('Qual o número que vc quer fazer o fatorial? ')),show = True)