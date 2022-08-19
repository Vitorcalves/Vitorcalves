"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 16/08/2022 as 19:02
FINALIDADE: 2)

"""

listaNome = []
listaIdade = []

xNova = -1			# Indice da pessoa mais nova
xVelha = -1			# Indcie da pessoa mais velha

for x in range(10):

	print(f"Informe os dados para a pessoa no indice {x}")
	print()
	listaNome.append(input("Nome..: "))
	listaIdade.append(int(input("Idade.: ")))
	print("-" * 20)

	# apurando a pessoa mais nova e a pessoa mais velha

	if x == 0:
		xNova = x
		xVelha = x
	else:

		# apurando a pessoa mais nova

		if listaIdade[x] < listaIdade[xNova]:
			xNova = x

		# apurando a pessoa mais velha

		if listaIdade[x] > listaIdade[xVelha]:
			xVelha = x

print()
print("-" * 20)
print("Lista de pessoas")
print("-" * 30)

for x in range(len(listaNome)):
	print(f"{listaNome[x]} tem {listaIdade[x]} ano(s)")

print()
print()
print(f"A pessoa mais nova é {listaNome[xNova]} com {listaIdade[xNova]} ano(s)")

print(f"A pessoa mais velha é {listaNome[xVelha]} com {listaIdade[xVelha]} ano(s), e está no indice {xVelha}")