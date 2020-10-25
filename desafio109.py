from exr109 import moeda

p = float(input('Digite um valor de dinheiro: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% de {moeda.moeda(p)} é {moeda.diminuir(p, 13, True)}')