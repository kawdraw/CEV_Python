def aumentar(num, pcent):
    a = num * pcent / 100
    resultado = num + a
    return resultado


def diminuir(num, pcent):
    a = num * pcent / 100
    resultado = num - a
    return resultado


def dobro(num):
    a = num * 2
    return a


def metade(num):
    a = num / 2
    return a


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')