palavras = ('COCEIRA', 'GARGANTA', 'REMEDIO', 'GENGIBRE', 'CHA', 'BIROLIRO')
vogais = ('A', 'E', 'I', 'O', 'U')


for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais:', end='')
    vogaisEncontradas = ''

    for vogal in vogais:
        if vogal in palavra:
            vogaisEncontradas += ' '+vogal

    print(vogaisEncontradas)

