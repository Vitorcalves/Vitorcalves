# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

quant = int(input(" "))
print("informe a idade dos ",quant ," alunos")
idade = [int(input("insira a idade do aluno")) for x in range(quant)]
print('-'*50)
print("informe a altura dos ",quant ," alunos")
# altura = [int(input("insira a altura do aluno")) for x in range(quant)]
altura = []
media = 0
for x in range(quant):
    altura.append(int(input("insira a altura do aluno")))
    media = media + altura[x]

media = media / quant
for y in range(len(idade)):
    