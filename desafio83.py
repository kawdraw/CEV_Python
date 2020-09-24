exprecao = input('Digite uma expreção com o uso de parenteses: ')

pilha = list()

for simb in exprecao:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expreção válida')
else:
    print('Expreção invalida')