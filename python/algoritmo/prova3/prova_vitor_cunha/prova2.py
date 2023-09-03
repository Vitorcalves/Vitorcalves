
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
jogador = []
ordenada = []
achou = False

while True:
	print("1 – Cadastrar pessoas")

	
	print("2 – Busca jogadores por nome")
	print("3 - Jogador mais velho (atacante)")
	print("4 – Listagem de jogadores por número de gols (apenas os que tem gols marcados)")
	print("5 – Sair do Sistema")
	print("6 – Média de idade das pessoas")
	print("7 - Sair")
	opc = int(input("Informe a opção Desejada: "))

	if opc == 1:

		if len(nome) >= 11:
			print()
			print("voce ja atingiu os 11 jogadores.")
			print()
		else:

			print()
			print("Informe os dados")
			print()

			nome = input("Nome ")
			idade = int(input("Idade "))
			while True:
				posicao = int(input("posicao 1=Goleiro, 2=Zagueiro, 3=Meio Campo, 4=Atacante"))
				if posicao == 1 or posicao == 2 or posicao == 3 or posicao == 4:
					break

			gol = int(input("número de gols marcados na temporada"))

			jogador.append([nome, idade, posicao, gol])

	elif opc == 2:
		buscaNome = str(input("Informe o nome que deseja pesquisar: "))



		for x in range(len(jogador)):
			if buscaNome == jogador[x][0][0]:
				print(f"Encontrado o nome {jogador[x][0][0]} no indice {x} da lista nome")
				achou = True

		if not achou:
			print(f"Nome {buscaNome} não localizado na lista nome")





		
	elif opc == 3:
		print("")

	
	
	elif opc == 4:
		for x in range(1, len(jogador)):
			for y in range(len(jogador) -1, 0, -1):
				if jogador[0][0][0][y] > jogador[0][0][0][y -1]:
					auxnu = jogador[0][0][0][y]
					aux1 = jogador[y]
					aux2 = jogador[y]
					aux3 = jogador[y]

					jogador[0][0][0][y] = jogador[0][0][0][y -1]
					jogador[0][0][y][0] = jogador[0][0][y -1][0]
					jogador[0][y][0][0] = jogador[0][y -1][0][0]
					jogador[y][0][0][0] = jogador[y -1][0][0][0]

					jogador[0][0][0][y -1] = auxnu
					jogador[0][0][y -1][0] = aux1
					jogador[0][y -1][0][0] = aux2
					jogador[y -1][0][0][0] = aux3







		for x in range(len(jogador)):
			print(f"{jogador[x]}")






	elif opc == 5:
		print("=" * 50)
		resp = input("Deseja realmente abandonar o APP (S/N): ")

		if resp.upper() == "S":
			break

	else:
		print("=" * 40)
		pause = input("Opção Inválida, pressione ENTER para continuar")		



