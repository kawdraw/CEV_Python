contador = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
for cont in contador:
    posicao = int(input('Digite um número de 0 a 20: '))
    if posicao < 0 or posicao > 20:
        continue
    print(contador[posicao])
    break