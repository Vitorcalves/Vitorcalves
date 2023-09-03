"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 27/09/2022 as 18:30
FINALIDADE: Crie um programa que vai ler vários números e colocar em uma lista. 
			Depois disso, mostrar:
				a) Quantos números foram digitados.
				b) A lista de valores ordenada de forma decrescente.
				c) Quantos valores pares foram digitados na lista e os respectivos valores.
			OBS: Este programa não deverá conter o menu de opções.
"""

aNumero = []
qtdPar = 0

while True:

	num = int(input("Informe um valor (ou zero para sair): "))

	if num == 0:
		break
	else:
		aNumero.append(num)

# 

print("=" * 30)
print(f"Foram digitados {len(aNumero)} valores")

# Ordenando a lista de forma decrescente

for x in range(1, len(aNumero)):
	for y in range(len(aNumero) -1, 0, -1):
		if aNumero[y] > aNumero[y -1]:
			aux 			= aNumero[y]
			aNumero[y] 		= aNumero[y -1]
			aNumero[y -1] 	= aux

print("=" * 30)
print("Lista de valores em ordem decrescente")
print()

for x in range(len(aNumero)):
	print(f"{aNumero[x]}")

print("=" * 30)
print("Lista de valores pares")
print()

for x in range(len(aNumero)):
	# apurando se o valor é par
	if (aNumero[x] % 2) == 0:
		print(f"{aNumero[x]}")
		qtdPar += 1

print()
print(f"Foram digitados {qtdPar} valores pares")
print()