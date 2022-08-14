# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = list(int(input("insira o valor")) for x in range (5))
soma = 0 
multipli = 1
for x in range(len(numeros)):
    soma = soma + numeros[x]
for x in range(len(numeros)):
    multipli = multipli * numeros[x]
print(f"a soma dos valores e {soma} ")
print("a multiplicacao dos valores e de ",multipli )
print("os valores sao",numeros)




