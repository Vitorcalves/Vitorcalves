"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 19/09/2022 as 20:27
FINALIDADE: 9) Solicite ao usuário a entrada de 10 valores 
				inteiros, armazene estes valores em uma lista. 
				No final classifique em ordem crescente e
				exiba os valores.
"""

valores = []

for i in range(10):
	valores.append(int(input("Digite um valor: ")))

# Ordena os valores em ordem crescente

for x in range(1, len(valores)):
	for y in range(len(valores) - 1, 0, -1):
		if valores[ y ] < valores[y -1]:
			aux 			= valores[y]
			valores[y]		= valores[y - 1]
			valores[y -1 ] 	= aux

# exibe os valores
print("=" * 30)
print("Listando os valores em ordem crescente")
print("=" * 30)

for x in range(len(valores)):
	print(f"{valores[x]}")

print("=" * 30)