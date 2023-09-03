resultado = []
informacoes = {}

from random import randint

for x in range(5):

	print("INFORME O NOME DO JOGADOR")
	informacoes['nome']  = input("Nome..: ")
	informacoes['nDado'] = int(input("Número: "))
	print("=" * 40)

	resultado.append(informacoes.copy())

for x in range(1, len(resultado)):
	for y in range(len(resultado) - 1, 0, -1):
		if resultado[y]['nDado'] < resultado[y - 1]['nDado']:
			aux          = resultado[y]
			resultado[y] = resultado[y - 1]
			resultado    = aux

for informacoes in resultado: 
	print(f"Jogador: {informacoes['nome']}")
	print(f"Número.: {informacoes['nDado']}")
	print("=" * 40)

print("JOGADOR CAMPEÃO:")
print(f"{informacoes[0]['nome']}, com o número {informacoes[0]['nDado']}")
print("=" * 40)