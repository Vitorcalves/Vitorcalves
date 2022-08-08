# exemplo tuplas
tAlunos = ('a', 'b', 'c')

print(tAlunos[2])

tAlunos = ('Carla', 'Joao', 'Joelma', 'Vitor')

print(tAlunos[2])

print("-" * 60)

print(f"Quantiddade de valores na tupla: {len(tAlunos)}")

ind = 0

while ind < len(tAlunos):
    print(f"alunos no indice {ind} e {tAlunos[ind]}")
    ind += 1

print("-" * 60)

for x in range(len(tAlunos)):
    print(f"aluno no indice {x} e {tAlunos[x]}")

print("-" * 60)

for nome in tAlunos:
    print(f"Alunos: {nome}")

print("-" * 60)
print("Percorre a tupla com enumerate")
print("-" * 60)

for pos, nome in enumerate(tAlunos):
	print(f"{nome} está no índice {pos}")
