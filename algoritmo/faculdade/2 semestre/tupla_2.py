# # Crie um programa que vai gerar dez números aleatórios e colocarem uma tupla. Depois disso mostre a listagem de númerosgerados e também indique o menor e o maior valor que estão natupla.

from random import randint

# # print(randint(0,10))
numeros = [randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100)]

# print(aleatorio)

menor = 0
maior = 0


# print(menor)

for x in range(len(numeros)):
    print(f"{numeros[x]}")
    if x == 0:
        menor = numeros[x]
        maior = numeros[x]
    else:
        if numeros[x] > maior:
            maior = numeros[x]
        if numeros[x] < menor:
            menor = numeros[x]
print(menor)
print(maior)