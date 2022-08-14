# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numeros = list()
par = list()
impar = list()
n=20
for x in range(n):
    numeros.insert(0, n)
    if (n % 2) == 0:
        par.insert(0,n)
    else:
        impar.insert(0,n)
    n -=1 
    
print(impar)
print(numeros)
print(par)

