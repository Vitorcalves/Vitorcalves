"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 16/08/2022 as 19:02
FINALIDADE: 1) Faça um programa que leia 5 valores numéricos e grave em
uma lista. Ao final mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.
"""

listaValor = []

menorValor = 0
maiorValor = 0

posMenorValor = -1
posMaiorValor = -1

for x in range(5):

	listaValor.append(int(input("Informe um valor: ")))

	# Apurando o menor e o maior valor

	if x == 0:
		menorValor = listaValor[x]
		maiorValor = listaValor[x]

		posMenorValor = x
		posMaiorValor = x
	else:

		# apurar o menor valor

		if listaValor[x] < menorValor:
			menorValor = listaValor[x]
			posMenorValor = x

		# apurar o maior valor

		if listaValor[x] > maiorValor:
			maiorValor = listaValor[x]
			posMaiorValor = x

# exibir a lista

print()
print()
print("Listando os valores digitados:")
print()

for x in range(len(listaValor)):
	print(listaValor[x])

print("-" * 10)
print(f"O menor valor é {menorValor} e está no indice {posMenorValor}")
print(f"O maior valor é {maiorValor} e está no indice {posMaiorValor}")