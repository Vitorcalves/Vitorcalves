# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idade = []
altura = []

for x in range(5):
    print("informe os dados")
    idade.append(int(input("insira a idade")))
    altura.append(float(input("insira a altura")))
for y in range(len(idade)):
    print(f"a idade da {y + 1} ° pessoa e {idade[y]} e altura {altura[y]}")
    