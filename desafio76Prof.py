listaDeCompras = ('Banana', 2.50, 'Achocolatado', 7.00, 'Pão', 4.00, 'Panela', 150.00, 'Tesoura', 15.00,)
linha = '-' * 40
print(linha)
print(f'{"LISTA DE COMPRAS":^40}')
print(linha)

for id in range (0, len(listaDeCompras), 2):
    print(f'{listaDeCompras[id]:.<30}', end='')
    print(f'R${listaDeCompras[id+1]:>8.2f}')
print(linha)

