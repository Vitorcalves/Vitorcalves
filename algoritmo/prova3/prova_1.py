# (4,0 pontos). Crie um programa onde 5 jogadores joguem um dado e tenham resultados 
# aleatórios (poderá ser digitado ou gerado aleatoriamente). Guarde esses resultados em 
# um dicionário. No final, apresente este dicionário em ordem (maior valor tirado no dado
# para o menor valor), sabendo que o vencedor tirou o maior número no dado

import random
valor = 0
resultado = []
dado = dict()
for x in range (5) :
    dado['nome']  = input("Nome ")
    valor = int(input("digite o resultado do dado ou 0 para um resultado aleatorio "))
    if valor == 0:
        valor = random.random(1,6)
    dado['numero'] = valor

    resultado.append(dado.copy())

for x in range(1, len(resultado)):
	for y in range(len(resultado) - 1, 0, -1):
		if resultado[y:y] < resultado[y - 1 : y]:
			aux = resultado[y]
			resultado[y] = resultado[y - 1]
			resultado    = aux

for informacoes in resultado: 
	print(f"jogador: {informacoes['nome']}")
	print(f"Número.: {informacoes['numero']}")
	print("=" * 40)

print("JOGADOR CAMPEÃO:")
print(f"{informacoes[0]['nome']}, com o número {informacoes[0]['numeor']}")
print("=" * 40)


