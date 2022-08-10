from re import X


valor = tuple(int(input("insira o valor")) for x )

print(valor[X])

while True:
    busca = 5

    achou = 0

    for n in range(len(valor)):
        if valor[n] == busca:
            achou += 1
            
    print(f"o valor 5 aparece {busca} vezes")

    # if not achou:
    #     print("o piloto nao foi localizado")

