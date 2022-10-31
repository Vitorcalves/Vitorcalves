# (4,0 pontos). Crie um programa onde 5 jogadores joguem um dado e tenham resultados 
# aleatórios (poderá ser digitado ou gerado aleatoriamente). Guarde esses resultados em 
# um dicionário. No final, apresente este dicionário em ordem (maior valor tirado no dado
# para o menor valor), sabendo que o vencedor tirou o maior número no dado.
import random
resultado = []
dado = {}
for x in range (5):
    dado['nome'] = input("digite seu nome ")
    valor = int(input("digite o valor do dado ou 0 para um valor aleatorio "))
    if valor == 0:
        valor = random.randint(1,6)
    dado['valores'] =valor
    valor= 0

    resultado.append(dado.copy())

for x in range(len(resultado)):
	print(f"{resultado[x]}")

for x in range(1, len(resultado)):
	for y in range(len(resultado) -1, 0, -1):
		if resultado[y]["valores"] > resultado[y -1]["valores"]:
			auxnu = resultado[y]["valores"]
			auxno = resultado[y]["nome"]

			resultado[y]["valores"] = resultado[y -1]["valores"]
			resultado[y]["nome"] = resultado[y -1]["nome"]

			resultado[y -1]["valores"] = auxnu
			resultado[y -1]["nome"] = auxno

print("Lista de valores do dado ")
print()
for x in range(len(resultado)):
	print(f"{resultado[x]}")

print(f'o vencedor e {resultado[0]}' )

