listavalor = []

menorvalor = 0
maiorvalor = 0

for x in range(5):
    listavalor.append(int(input("informe um valor: ")))

    # apurando o menor e o maior valor

    if x == 0:
        menorvalor = listavalor[x]
        maiorvalor = listavalor[x]

        posmenorvalor = x
        posmaiorvalor = x
    else:
        # apurar o menor valor
        if listavalor[x] < menorvalor:
            menorvalor = listavalor[x]
            posmenorvalor = x

        # apurar o maior valor
        if listavalor[x] > maiorvalor:
            maiorvalor = listavalor[x]
            posmaiorvalor = x
            
