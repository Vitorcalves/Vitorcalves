"""
AUTO......: Aldecir Fonseca
DATA/HORA.: 21/06/2022 as 19:08
FINALIDADE:
			38) Uma empresa concederá um aumento de salário aos seus
			funcionários, variável de acordo com o cargo, conforme a tabela
			abaixo. Faça um algoritmo que leia o salário e o cargo de 5 
			funcionário e calcule o novo salário. Se o cargo do funcionário 
			não estiver na tabela, ele deverá, então, receber 40% de aumento. 
			Mostre o salário antigo, o novo salário e a diferença para cada 
			funcionário. No final apresente o valor total da folha antes 
			do reajuste e depois do reajuste.

			COGIGO	DESCRIÇÃO				%
			101		Gerente					10
			102		Engenheiro				20
			103		Técnico					30
"""

totalAntesReajuste  = 0
totalDepoisReajuste = 0

for x in range(5):

	print('===================================')
	print('COGIGO	DESCRIÇÃO				% ')
	print('-----------------------------------')
	print('101		Gerente					10')
	print('102		Engenheiro				20')
	print('103		Técnico					30')
	print('???		Outros                  40')
	print('-----------------------------------')

	cargo = int(input("Informe o cargo: "))
	salario = float(input("Informe o salário: "))

	if cargo == 101:
		percReajuste = 10
	elif cargo == 102:
		percReajuste = 20
	elif cargo == 103:
		percReajuste = 30
	else:
		percReajuste = 40

	salarioNovo = salario + round((salario * percReajuste) / 100, 2)
	totalAntesReajuste += salario
	totalDepoisReajuste += salarioNovo

	print("-" * 50)
	print(f"Salário antes do reajuste  R$ {salario:>12.2f}")
	print(f"Valor do reajuste salarial R$ {(salarioNovo - salario):>12.2f}")
	print(f"Salário depois do reasjute R$ {salarioNovo:>12.2f}")
	print()
	print()
	print()

#
print("=" * 50)
print(f"TOTAL DA FOLHA ANTES DO REAJUSTE  R$ {totalAntesReajuste:>12.2f}")
print(f"TOTAL DA FOLHA DEPOIS DO REAJUSTE R$ {totalDepoisReajuste:>12.2f}")
print("=" * 50)