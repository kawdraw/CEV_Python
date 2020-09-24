def área (largura, comprimento):
    resultado = largura * comprimento
    print(f'O terreno de {largura}m de largura e {comprimento}m de comprimento tem como área {resultado}m²')


largura = float(input('Lagura do terreno em Metros: '))
comprimento = float(input('Comprimento do terreno em Metros: '))
área(largura, comprimento)