# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
cont = 4
notas = list(float(input("insira as notas dos alunos: ")) for x in range(cont))
soma = 0
for x in range(len(notas)):
    soma = soma + notas[x]
media = soma / 4
print(f"sua media e {media}")