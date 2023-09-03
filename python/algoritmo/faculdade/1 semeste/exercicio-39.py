"""
AUTO......: Aldecir Fonseca
DATA/HORA.: 21/06/2022 as 19:35
FINALIDADE:
			39) Escrever um algoritmo que leia o nome e o sexo de 15
			pessoas, ao final determine:
				• Total de homens e de mulheres.
				• A mulher mais nova
				• O homem mais velho
				• A média de idade de todas as pessoas
"""

totHomens = 0
totMulheres = 0

mulherNovaIdade = 0
mulherNovaNome = ''

homenVelhoIdade = 0
homenVelhoNome = ''

somaIdade = 0

for x in range(5):

	print("-" * 50)
	print(f"Informe os seguintes dados: {(x + 1)}")
	print('-' * 50)

	nome = input("Nome......: ")

	while True:
		sexo = input("Sexo (M=Masculino; F=Feminino): ")

		if sexo.upper() == "M" or sexo.upper() == "F":
			break
		else:
			print("Sexo inválido, informe um sexo válido para continuar...")

	idade = int(input("Idade: "))

	# acumulando o total de pessoas conforme o sexo

	if sexo.upper() == "M":
		totHomens += 1

		# Apurando o homem mais velho
		if idade > homenVelhoIdade or totHomens == 1:
			homenVelhoNome = nome
			homenVelhoIdade = idade

	elif sexo.upper() == "F":
		totMulheres 

		# apurar a mulher mais nova
		if idade < mulherNovaIdade or totMulheres == 1:
			mulherNovaNome = nome
			mulherNovaIdade = idade

	# acumular a idade de todas as pessoas
	somaIdade += idade

#

print("=" * 50)
print(f"Total de homens informados é {totHomens}")
print(f"Total de mulheres informados é {totMulheres}")
print(f"A mulher mais nova é {mulherNovaNome}, e tem {mulherNovaIdade} anos(s)")
print(f"O homem mais velho é {homenVelhoNome}, e tem {homenVelhoIdade} anos(s)")
print(f"A média da idade das pessoas informadas é {round((somaIdade / (x + 1)), 1)}")
print("=" * 50)