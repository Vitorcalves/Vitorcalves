# (6,0 pontos). Escreva um programa que solicita ao usuário o nome, o sexo e a idade de 
# 12 pessoas, armazene estes dados em listas:
# Crie o menu de opções abaixo:
# 1 – Cadastrar pessoas
# 2 – Listagem de pessoas do sexo feminino em ordem alfabética
# 3 – Listagem de pessoas por idade (decrescente)
# 4 – Quantidade pessoas por sexo
# 5 – Homem mais velho e o índice onde o mesmo está localizado
# 6 – Média de idade das pessoas
# 7 - Sair

from pickle import TRUE


nome = []
sexo = []
idade = []
mulher = []
media = 0



while True:
	print("=" * 30)
	print("MENU DE OPÇÕES")
	print()
	print("1) Cadastrar pessoa")
	print("2) Listagem de pessoas do sexo feminino em ordem alfabética")
	print("3) Listagem de pessoas por idade (decrescente)")
	print("4) Quantidade pessoas por sexo")
	print("5) Homem mais velho e o índice onde o mesmo está localizado")
	print("6) Média de idade das pessoas")
	print("7) Sair")

	print("-" * 30)

	opc = int(input("Informe a opção desejada: "))  

	if opc == 1:
		testesexo = ""
		testenome = ""

		if len(nome) > 12:
			print("#" * 30)
			print("Limite de pessoas cadastradas já foi atingido.")
			print("#" * 30)
		else:
			print()
			print("#" * 30)
			
			print(f"Informe os dados para a pessoa {len(nome) + 1}")
			testenome = input("Nome...: ")
			nome.append(testenome)
			idade.append(int(input("Idade..: ")))
			testesexo = (input("digite M para o sexo masculino e F para o feminino: "))
			while True:
				if testesexo.upper() == "M" or testesexo.upper() == "F":
					sexo.append(testesexo.upper())
					break 
				else:
					print("Valor digitado invalido")
					testesexo = (input("digite M para o sexo masculino e F para o feminino"))
			if testesexo.upper() == "F":
				mulher.append(testenome)

	elif opc == 2:
		if len(mulher) == 0:
			print("#" * 30)
			print("Não existem mulheres cadastradas.")
			print("#" * 30)
		else:

			for x in range(1, len(mulher)):
				for y in range(len(mulher) -1 , 0 , -1):
					if mulher[y] < mulher[y - 1]:
						auxNome		= mulher[y]
						mulher[y]		= mulher[y -1 ]
						mulher[y -1 ] = auxNome

			print("#" * 30)
			print("Listagem de mulheres em ordem alfabetica")
			print()
			print("NOME              ")
			print("#" * 30)

			for x in range(len(mulher)):
				print(f"{mulher[x].ljust(20)}")

			print("#" * 30)

	elif opc == 3:

		if len(nome) == 0:
			print("#" * 30)
			print("Não existem pessoas cadastradas.")
			print("#" * 30)
		else:
			for x in range(1, len(nome)):
				for y in range(len(nome) -1 , 0 , -1):
					if idade[y] > idade[y - 1]:
						auxNome		= nome[y]
						nome[y]		= nome[y -1 ]
						nome[y -1 ] = auxNome

						auxIdade		= idade[y]
						idade[y]		= idade[y -1 ]
						idade[y -1 ] 	= auxIdade

			# exibindo os dados

			print("#" * 30)
			print("Listagem de pessoas em idade decrescente")
			print()
			print("NOME                  IDADE")
			print("#" * 30)

			for x in range(len(nome)):
				print(f"{nome[x].ljust(20)}  {idade[x]}")

			print("#" * 30)

	elif opc == 4:

		print("=" * 30)
		print("Quantidade pessoas por sexo")
		print()
		print(len(mulher), "mulheres" ,len(nome) - len(mulher),"homes")


	elif opc == 5:
		print("Homem mais velho e o índice onde o mesmo está localizado")
		for x in range(len(idade)):
				if x == 0:
				
					idademaior = x
				else:
					if idade[x] > idade[idademaior]:
						idademaior = x
		print("pessoa mais velha",idademaior)

	elif opc == 6:
		print("=" * 30)
		print("Média de idade das pessoas")
		print()
		for x in range(len(idade)):
			media += idade[x]
		media = media / len(idade)
		print("a media de idade e ", idade)








	elif opc == 7:

		resp = input("Deseja abandonar o APP (S/N): ")

		if resp.upper() == "S":
			break

	else:
		print("#" * 30)
		print("Opção informada é inválida...")
		print("#" * 30)