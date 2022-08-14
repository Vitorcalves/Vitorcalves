# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
# aluno1 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno2 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno3 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno4 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno5 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno6 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno7 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno8 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno9 = list(float(input("insira as notas do aluno " )) for x in range(4))
# aluno10 = list(float(input("insira as notas do aluno " )) for x in range(4))

alunos = list()

for x in range(10):
    total = 0
    print("digite a nota do proximo aluno")
    for x in range(4):
        nota = float(input("insira as notas do aluno"))
        total = nota + total
    total = total/4
    alunos.insert(10, total)
for y in range(len(alunos)):
    if alunos[y] >= 7:
        print(f"os alunos aprovados sao {y + 1:>2.0f}° com {alunos[y]} pontos")
