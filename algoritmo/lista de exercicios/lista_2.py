# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
tupla = tuple(float(input("insira os des valores")) for x in range (10))
cont = 9
for x in range(len(tupla)):
    print(f"{tupla[cont]}")
    cont -= 1
