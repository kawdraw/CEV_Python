def aumentar(num, pcent, formato = False):
    a = num * pcent / 100
    resultado = num + a
    return resultado if formato is False else moeda(resultado)


def diminuir(num, pcent, formato = False):
    a = num * pcent / 100
    resultado = num - a
    return resultado if formato is False else moeda(resultado)


def dobro(num, formato = False):
    a = num * 2
    return a if formato is False else moeda(a)


def metade(num, formato = False):
    a = num / 2
    return a if formato is False else moeda(a)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')