# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
A  = [int(input("insira um numero inteiro")) for x in range(10)]
total = 0
for x in range(len(A)):
    total = total + A[x] * A[x]
print(f"a soma dos quadrados e {total}")

