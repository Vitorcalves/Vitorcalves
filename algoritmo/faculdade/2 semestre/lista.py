# lista vazia

listavazia = []

listavazia2 = list()

listaalunos = ["maariaa", "carinha", "tropa"]

print(listaalunos[2])

cont = 0

while cont <= len (listaalunos):
    print(f"{listaalunos[cont]}")
    cont += 1

# adicinando termos a lista
listaalunos.append("pedro")
listaalunos.append(input("informe o nome do aluno"))

listaalunos.insert(1, "eduardo")

# remover nome da lista

listaalunos.remove(input())

for i in range(len(listaalunos)):
    print(f"{listaalunos[i]}")

# remove aluno em um indice determindo

listaalunos.pop(1)

# limpa llista

listaalunos.clear

