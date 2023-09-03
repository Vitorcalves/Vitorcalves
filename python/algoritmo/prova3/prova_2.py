# (6,0 pontos). O TFC (Tabajara Futebol Clube) solicitou a turma de 2º período de ADS da 
# FASM que elabore um software para gerenciar os dados de seus jogadores titulares (11 
# jogadores). Para cadastrar um jogador deve-se fornecer: Nome, Idade, Posição 
# (1=Goleiro; 2=Zagueiro; 3=Meio Campo; 4=Atacante) e número de gols marcados na 
# temporada, armazene estes dados uma matriz.
# Escreva um programa que apresente o seguinte menu ao usuário: 
# 1 – Cadastrar Jogador
# 2 – Busca jogadores por nome
# 3 - Jogador mais velho (atacante)
# 4 – Listagem de jogadores por número de gols (apenas os que tem gols marcados)
# 5 – Sair do Sistema
# Para a opção 1, solicite os dados e armazene em uma única matriz todos os dados. 
# Para a opção 2, criar a possibilidade de realizar uma busca por nome do jogador, caso a 
# busca encontre mais de um jogador deverá exibir todos os jogadores localizados, se não 
# encontrar deverá ser exibido uma mensagem ao usuário informando que não foi possível 
# localizar jogadores para a busca solicitada.
# Para a opção 3, exiba os dados do jogador e o índice onde ele se encontra no momento, 
# para o atacante mais velho. 
# Para a opção 4, exiba uma listagem com todos os dados dos jogadores que marcaram 
# gols na temporada.
# Para a opção 5, apenas sair do sistema.

nome = []
idade = []
sexo = []

while True:

	print("------------------------------------------------------------")
	print("MENU DE OPÇÕES:")
	print("------------------------------------------------------------")
	print("1 – Cadastrar jogador")
	print("2 – Busca jogadores por nome")
	print("3 - Jogador mais velho (atacante)")
	print("4 – Listagem de jogadores por número de gols (apenas os que tem gols marcados)")
	print(" - Sair")
	print("------------------------------------------------------------")

	opc = int(input("Informe a opção Desejada: "))

	if opc == 1:

		if len(nome) >= 11:
			print("=" * 40)
			print("Quantidade de pessoas já atingiu 11.")
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
