# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
from re import X


print("insira os valores do primeiro vetor")
primeiro = [input("insira o vetor") for x in range(10)]
print("insira os valores do segundo vetor")
segundo = [input("inrira o valor") for x in range(10)]
terceiro = []
for x in range(len(primeiro)):
    terceiro.append(primeiro[x])
    terceiro.append(segundo[x])

print(terceiro)