# https://www.pythonprogressivo.net/2018/10/Exercicio-Sequencias-Listas-Tuplas-Dicionarios.html
# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
cont = int(input("insira a quantidade de numeros voce ira inserir "))
tupla = tuple(int(input("insira o " + str(x + 1) + "° : " ))for x in range(cont))
print(tupla)
