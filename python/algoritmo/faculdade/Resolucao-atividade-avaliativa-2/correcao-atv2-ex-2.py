"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 27/09/2022 as 18:30
FINALIDADE: Escreva um programa que solicita ao usuário o nome, 
			o sexo e a idade de 12 pessoas, armazene estes dados 
			em listas:

			Crie o menu de opções abaixo:
				1 – Cadastrar pessoas
				2 – Listagem de pessoas do sexo feminino em ordem alfabética
				3 – Listagem de pessoas por idade (decrescente)
				4 – Quantidade pessoas por sexo
				5 – Homem mais velho e o índice onde o mesmo está localizado
				6 – Média de idade das pessoas
				7 - Sair
"""

nome = []
idade = []
sexo = []

while True:

	print("------------------------------------------------------------")
	print("MENU DE OPÇÕES:")
	print("------------------------------------------------------------")
	print("1 – Cadastrar pessoas")
	print("2 – Listagem de pessoas do sexo feminino em ordem alfabética")
	print("3 – Listagem de pessoas por idade (decrescente)")
	print("4 – Quantidade pessoas por sexo")
	print("5 – Homem mais velho e o índice onde o mesmo está localizado")
	print("6 – Média de idade das pessoas")
	print("7 - Sair")
	print("------------------------------------------------------------")

	opc = int(input("Informe a opção Desejada: "))

	if opc == 1:

		if len(nome) >= 12:
			print("=" * 40)
			print("Quantidade de pessoas já atingiu 12.")
			print("=" * 40)
		else:

			print("=" * 40)
			print("Informe os dados")
			print("=" * 40)

			nome.append(input("Nome......: "))
			idade.append(int(input("Idade.....: ")))
			sexo.append(input("Sexo (M/F): "))

	elif opc == 2:

		# ordenando pessoas
		for x in range(1, len(nome)):
			for y in range(len(nome) -1 , 0 , -1):
				if nome[y] < nome[y -1]:
					auxNome 	= nome[y]
					nome[y]		= nome[y -1]
					nome[y -1]	= auxNome

					auxIdade 	= idade[y]
					idade[y]	= idade[y -1]
					idade[y -1]	= auxIdade

					auxSexo 	= sexo[y]
					sexo[y]		= sexo[y -1]
					sexo[y -1]	= auxSexo

		# lista de Mulheres

		print("=" * 40)
		print("Litagem de Mulheres (ordem alfabética")
		print()
		print("NOME                  IDADE  SEXO")
		print("=" * 40)

		for x in range(len(nome)):
			if sexo[x].upper() == "F":
				print(f"{nome[x]:<20}  {idade[x]:>5.0f}  {sexo[x]}")

		print("=" * 40)
		pause = input("Pressione ENTER para continuar")

	elif opc == 3:

		# ordenando pessoas por idade decrescente
		for x in range(1, len(nome)):
			for y in range(len(nome) -1 , 0 , -1):
				if idade[y] > idade[y -1]:
					auxNome 	= nome[y]
					nome[y]		= nome[y -1]
					nome[y -1]	= auxNome

					auxIdade 	= idade[y]
					idade[y]	= idade[y -1]
					idade[y -1]	= auxIdade

					auxSexo 	= sexo[y]
					sexo[y]		= sexo[y -1]
					sexo[y -1]	= auxSexo

		# lista de pessoas

		print("=" * 40)
		print("Litagem das pessoas (ordem de idade decrescente)")
		print()
		print("NOME                  IDADE  SEXO")
		print("=" * 40)

		for x in range(len(nome)):
			print(f"{nome[x]:<20}  {idade[x]:>5.0f}  {sexo[x]}")

		print("=" * 40)
		pause = input("Pressione ENTER para continuar")

	elif opc == 4:

		qtdMasculino = 0
		qtdFeminino = 0

		print("=" * 40)
		print("Quantidade de pessoas por sexo")
		print("=" * 40)

		for x in range(len(sexo)):
			if sexo[x].upper() == "M":
				qtdMasculino += 1
			elif sexo[x].upper() == "F":
				qtdFeminino += 1

		print(f"Total de Homens {qtdMasculino}")
		print(f"Total de Mulheres {qtdFeminino}")

		print("=" * 40)
		pause = input("Pressione ENTER para continuar")	

	elif opc == 5:

		if len(nome) > 0:

			indMaisVelho = -1

			print("=" * 40)
			print("Homen mais velho")
			print("=" * 40)

			for x in range(len(nome)):
				if sexo[x].upper() == "M":
					if indMaisVelho == -1:
						indMaisVelho = x
					else:
						if idade[x] > idade[indMaisVelho]:
							indMaisVelho = x

			print(f"O homen mais velho é {nome[indMaisVelho]} com {idade[indMaisVelho]} ano(s) e está no indice {indMaisVelho}")

		else:
			print("=" * 40)
			print("Ainda não foram cadastradas pessoas")

		print("=" * 40)
		pause = input("Pressione ENTER para continuar")	

	elif opc == 6:

		if len(nome) > 0:

			soma = 0

			for x in range(len(idade)):
				soma += idade[x]

			print("=" * 40)
			print(f"A média de idades das pessoas digitadas é {(soma / len(idade)):<6.2f}")
		
		else:
			print("=" * 40)
			print("Ainda não foram cadastradas pessoas")
					
		print("=" * 40)
		pause = input("Pressione ENTER para continuar")	

	elif opc == 7:
		print("=" * 50)
		resp = input("Deseja realmente abandonar o APP (S/N): ")

		if resp.upper() == "S":
			break

	else:
		print("=" * 40)
		pause = input("Opção Inválida, pressione ENTER para continuar")		



