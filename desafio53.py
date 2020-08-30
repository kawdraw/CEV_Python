text = str(input('Digite algum texto para ver se é Palindromo: '))
text = text.strip()
text = text.upper()
listaText = text.split()
junto = ''.join(listaText)
ehPalindromo = junto == junto [::-1]

if (ehPalindromo):
    print ('É um palindromo!')
else:
    print('Não é um palindromo!')

stringLength = len (junto)
reveseString = text [stringLength::-1]

ehIgual = 'iguais'
if (not ehPalindromo):
    ehIgual = 'diferentes'

print('Pois seguintes palavras {} e o seu contrario {}, são {}.'.format(text, reveseString, ehIgual))