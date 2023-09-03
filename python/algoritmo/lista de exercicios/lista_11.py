# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

from re import X


print("insira os valores do primeiro vetor")
primeiro = [input("insira o vetor") for x in range(10)]
print("insira os valores do segundo vetor")
segundo = [input("inrira o valor") for x in range(10)]
print("insira os valores do terceiro vetor")
terceiro = [input("inrira o valor") for x in range(10)]
quarto = []
for x in range(len(primeiro)):
    quarto.append(primeiro[x])
    quarto.append(segundo[x])
    quarto.append(terceiro[x])


print(quarto)