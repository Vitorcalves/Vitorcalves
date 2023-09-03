"""
Exemplo dicionario - 3
"""

agenda = []			# lista
contato = {}		# dicionario

aSexo = {'M': 'Masculino', 'F' : 'Feminino'}

while True:
	print("Informe os dados para Contato:")
	print()
	contato['nome'] = input("Nome......: ")
	contato['sexo'] = input("Sexo (M/F): ")
	contato['idade'] = int(input("IDADE.....: "))
	print("-" * 50)

	agenda.append(contato.copy())

	resp = input("Deseja adicionar um novo contato (S/N)?: ")

	if resp.upper() == "N":
		break

# Ordenando as pessoas em ordem alfabética
for x in range(1, len(agenda)):
	for y in range(len(agenda) - 1, 0 , -1):
		if agenda[y]['nome'].upper() < agenda[y -1]['nome'].upper():
			aux 			= agenda[y]
			agenda[y] 		= agenda[y -1]
			agenda[y -1] 	= aux

# mostrar minha agenda

print('=' * 40)
print("Exibindo a agenda:")
print('=' * 40)

for contato in agenda:
	print("CONTATO:")
	print(f"NOME...: {contato['nome']}")
	print(f"SEXO...: {aSexo[contato['sexo'].upper()]}")
	print(f"IDADE..: {contato['idade']}")
	print("-" * 40)
