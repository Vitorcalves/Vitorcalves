"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 18/10/2022 as 18:43
FINALIDADE: 16) A direção da FASM quer agora informatizar 
			a biblioteca. Para começar ela quer que 
			todos os livros que estão nas estantes 
			sejam cadastrados no computador. Foi 
			decidido que as seguintes informações de 
			cada livro deveram ser armazenadas no 
			computador: Código, titulo, autor, ano de 
			edição e quantidade. 
			Crie um programa com uma interface que irá 
			receber os dados dos livros até o usuário 
			informe o código de livro igual a ZERO, 
			estes dados deverão ser armazenados em um 
			dicionário. Ao final determine e exiba os 
			dados do livro que possui a maior quantidade 
			de livros e o total de livros que a biblioteca 
			possui.
"""

livro = dict()			# dicionário de livros
biblioteca = list()		# lista de livros da biblioteca

totalLivros = 0
indMaiorQtd = -1

while True:
	print("Informe os dados do livro que deseja cadastrar:")
	print()
	livro['codigo'] = int(input("Código ou ZERO para sair: "))

	if livro['codigo'] == 0:
		break
	else:

		livro['titulo'] 	= input("TITULO....: ")
		livro['autor']		= input('AUTOR.....: ')
		livro['anoEdicao'] 	= input('ANO EDIÇÃO: ')
		livro['quantidade'] = int(input('QUANTIDADE: '))

		biblioteca.append(livro.copy())
		totalLivros += livro['quantidade']

		# apurando o livro com maior quantidade

		if len(biblioteca) == 1:
			indMaiorQtd = 0
		else:
			if biblioteca[len(biblioteca) - 1 ]['quantidade'] > biblioteca[indMaiorQtd]['quantidade']:
				indMaiorQtd = len(biblioteca) - 1

# 

print("=" * 40)
print(f"O livro com maior quantidade na biblioteca é {biblioteca[indMaiorQtd]['titulo']}, do autor {biblioteca[indMaiorQtd]['autor']}, que foi lançado no ano {biblioteca[indMaiorQtd]['anoEdicao']}")
print("=" * 40)
print(f"O total de livros na biblioteca é {totalLivros}")
print("=" * 40)

print()
print()
print("=" * 40)
print("Listagem dos livros da biblioteca")
print("-" * 40)
print("CODIGO  TITULO                AUTOR                 ANO  QUANTIDADE")
print("-" * 40)

for livro in biblioteca:
	print(f"{livro['codigo']:6.0f}", end="  ")
	print(f"{livro['titulo']:<20}", end="  ")
	print(f"{livro['autor']:<20}", end="  ")
	print(f"{livro['anoEdicao']}", end="  ")
	print(f"{livro['quantidade']:>10.0f}")
	
print("=" * 40)
