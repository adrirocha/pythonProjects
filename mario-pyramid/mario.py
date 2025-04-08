while True:
    tam = int(input("Digite o tamanho da pirâmide: "))
    if (tam < 1) or (tam > 8):
        continue
    else:
        cont = 1
        while cont <= tam:
            print(' '*(9-cont), '#'*cont, '', '#'*cont)
            cont += 1
        break
