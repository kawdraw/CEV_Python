maiorPeso = 0.0
menorPeso = 1000.0

for i in range (1, 6):
    peso = float(input(f"Qual o peso da {i}ª pessoa? "))
    if peso >= maiorPeso:
        maiorPeso = peso    
    else:
        menorPeso = peso    

print(f"O maior peso é {maiorPeso} e o menor peso é {menorPeso}")