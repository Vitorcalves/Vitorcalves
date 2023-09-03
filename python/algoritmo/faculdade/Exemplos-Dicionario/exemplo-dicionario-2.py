"""
Exemplo dicionario - 2
"""

agenda = []			# lista
contato = {}		# dicionario

contato = {'nome': 'Beatriz', 'sexo': 'F', 'idade': 20}

agenda.append(contato.copy())

contato = {'nome': 'Joao', 'sexo': 'M', 'idade': 17}

agenda.append(contato.copy())

contato = {'nome': 'antonio', 'sexo': 'M', 'idade': 22}

agenda.append(contato.copy())

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
	print(f"SEXO...: {contato['sexo']}")
	print(f"IDADE..: {contato['idade']}")
	print("-" * 40)
