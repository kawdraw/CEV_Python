def interativo (ajuda):
    check = ajuda
    while True:
        ajuda = input('\033[30;43mQual função você quer ajuda [Digite 0 para parar]:\033[m ')
        check = ajuda
        if ajuda.isnumeric():
            break
        elif ajuda.isalpha():
            print(f'\033[0;102m{help(ajuda)}\033[m')



interativo(1)