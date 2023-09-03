from re import X


valor = tuple(int(input("insira o valor " + str(x + 1) + ": ")) for x in range(8))



# while True:


achou = 0
busca = 5
for n in range(len(valor)):
    if valor[n] == busca:
        achou += 1

print(f"o valor 5 aparece {achou} vezes")

# 7 onde apareceu
print("o 7 foi encontrado em: ", end="")
for y in range(len(valor)):
    if valor[y] == 7:
        print(f"{y}", end=", ")

print(" ")

# quais foram valores pares
print("os valores pares sao", end="")

for y in range(len(valor)):
    if (valor[y] % 2) == 0:
        # % e mode
        print(f"{valor[y]}", end=", ")





    # if not achou:
    #     print("o piloto nao foi localizado")

