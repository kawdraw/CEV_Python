somaDosProdutos = 0
produtosMais1000 = 0
produtoBarato = ''
menorValor = 9999999999999999999999
while True:
    nome = input('Qual o nome do produto: ')
    valor = float(input('Qual o valor do produto: '))
    verificacao = input('Deseja continuar[S/N]: ').upper()

    somaDosProdutos += valor
    if valor > 1000:
        produtosMais1000 += 1
    if valor <= menorValor:
        menorValor = valor
        produtoBarato = nome
    if verificacao != 'S':
        break
print(f'O valor gasto foi {somaDosProdutos}\nForam {produtosMais1000} que custaram mais de R$1000\nO nome do produto mais barato {produtoBarato}')