listaDeCompras = ('Banana', 2.50, 'Achocolatado', 7.00, 'Pão', 4.00, 'Panela', 150.00, 'Tesoura', 15.00,)
linha = '-' * 40
pontinnhos = '.' * 31
espacosNome = ' ' * 12
nomeCabecalho = 'LISTA DE COMPRAS'
cabecalho = f'{linha}\n{espacosNome}{nomeCabecalho}{espacosNome}\n{linha}'
moeda = 'R$ {}'

print(cabecalho)

for id in range (0, len(listaDeCompras), 2):
    nome = listaDeCompras[id]
    preco = '{0:.2f}'.format(listaDeCompras[id+1])
    tamanhoPreco = len(preco)

    if (tamanhoPreco < 6):
        resto = 6 - tamanhoPreco
        espacosEmBranco = ' ' * resto
        preco = moeda.format(espacosEmBranco + preco)
    else:
        preco = moeda.format(preco)

    nome = nome + pontinnhos[len(nome):] + preco
    print(nome)

print(linha)



