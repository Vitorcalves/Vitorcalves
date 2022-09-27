"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 19/09/2022 as 20:44
FINALIDADE: 10) Solicite ao usuário o nome e a idade 
			de 10 pessoas, armazene em listas. Crie um 
			menu de opções:
			1) Cadastrar pessoa
			2) Exibir em ordem crescente de Nome
			3) Exibir em ordem decrescente de Idade.
			4) Sair
"""

nome = []
idade = []

while True:
	print("=" * 30)
	print("MENU DE OPÇÕES")
	print()
	print("1) Cadastrar pessoa")
	print("2) Exibir em ordem crescente de Nome")
	print("3) Exibir em ordem decrescente de Idade.")
	print("4) Sair")
	print("-" * 30)
	opc = int(input("Informe a opção desejada: "))

	if opc == 1:

		if len(nome) > 10:
			print("#" * 30)
			print("Limite de pessoas cadastradas já foi atingido.")
			print("#" * 30)
		else:
			print()
			print("#" * 30)
			print(f"Informe os dados para a pessoa {len(nome) + 1}")

			nome.append(input("Nome...: "))
			idade.append(int(input("Idade..: ")))

	elif opc == 2:

		if len(nome) == 0:
			print("#" * 30)
			print("Não existem pessoas cadastradas.")
			print("#" * 30)
		else:

			# ordenando as pessoas
			for x in range(1, len(nome)):
				for y in range(len(nome) -1 , 0 , -1):
					if nome[y] < nome[y - 1]:
						auxNome		= nome[y]
						nome[y]		= nome[y -1 ]
						nome[y -1 ] = auxNome

						auxIdade		= idade[y]
						idade[y]		= idade[y -1 ]
						idade[y -1 ] 	= auxIdade

			# exibindo os dados

			print("#" * 30)
			print("Listagem de pessoas em ordem alfabetica")
			print()
			print("NOME                  IDADE")
			print("#" * 30)

			for x in range(len(nome)):
				print(f"{nome[x].ljust(20)}  {idade[x]}")

			print("#" * 30)

	elif opc == 3:

		if len(nome) == 0:
			print("#" * 30)
			print("Não existem pessoas cadastradas.")
			print("#" * 30)
		else:
			# ordenando as pessoas por idade decrescente
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
			print("Listagem de pessoas em ordem alfabetica")
			print()
			print("NOME                  IDADE")
			print("#" * 30)

			for x in range(len(nome)):
				print(f"{nome[x].ljust(20)}  {idade[x]}")

			print("#" * 30)

	elif opc == 4:

		resp = input("Deseja abandonar o APP (S/N): ")

		if resp.upper() == "S":
			break

	else:
		print("#" * 30)
		print("Opção informada é inválida...")
		print("#" * 30)