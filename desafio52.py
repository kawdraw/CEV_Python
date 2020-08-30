print('Cálculo de número primo')
nPrimo = int(input('Digite um número: '))
count = 0

for c in range (1, nPrimo, 1):
    if nPrimo % c == 0:
        print(f'\033[94m{c}', end=' ')
        count += 1
    else:
        print(f'\033[33m{c}', end=' ')

print(f'\033[92m{nPrimo}')

if count <= 2:
    print('\n\033[37mO número {} é primo!'.format(nPrimo))
else:
    print('\n\033[37mO número {} não é primo!'.format(nPrimo))