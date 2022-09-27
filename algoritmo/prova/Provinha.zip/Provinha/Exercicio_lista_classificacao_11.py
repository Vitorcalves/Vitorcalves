"""
	AUTOR.....: Aldecir Fonseca
	DATA/HORA.: 19/09/2022 AS 21:40
	FINALIDADE:
				11) Digite 15 nomes de pessoas no final permita o usuário digitar um nome que deseja verificar se existe nos 15 nomes digitados, caso exista exibir o nome e a posição na lista, caso contrário exibir mensagem de nome não localizado
"""

nome  		= list()
achou    	= False
buscaNome 	= ""

# Solicitando a lista de nomes

for x in range(5):
	nome.append(str(input("Digite um nome: ")))

# solicita nome a ser pesquisado

print("-" * 50)
buscaNome = str(input("Informe o nome que deseja pesquisar: "))
print("-" * 50)

# Efetua pesquisa na lista

for x in range(len(nome)):
	if buscaNome.upper() == nome[x].upper():
		print(f"Encontrado o nome {nome[x]} no indice {x} da lista nome")
		achou = True

if not achou:
	print(f"Nome {buscaNome} não localizado na lista nome")
