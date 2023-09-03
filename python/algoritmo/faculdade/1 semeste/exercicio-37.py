"""
AUTO......: Aldecir Fonseca
DATA/HORA.: 21/06/2022 as 18:45
FINALIDADE:
			37) O cardápio de uma lancheira é o seguinte

				CODIGO	DESCRICAO						PREÇO
				100		Cachorro Quente					 5,00
				101		Hamburger						12,00
				102		xBurguer						14,50
				103		xEggBurguer						16,00
				104		Cachorrão de salsicha			11,50
				105		xTudo							18,00

			Escrever um algoritmo que leia o código do item pedido, a 
			quantidade e calcule o valor a ser pago por aquele lanche. 
			O usuário poderá pedir quantos lanches desejar. Se informado 
			quantidade zero interrompe a execução e exibe o total do pedido.
"""

totalPedido = 0

print('----------------------------------------------')
print('CODIGO	DESCRICAO						PREÇO')
print('----------------------------------------------')
print('100		Cachorro Quente					 5,00')
print('101		Hamburger						12,00')
print('102		xBurguer						14,50')
print('103		xEggBurguer						16,00')
print('104		Cachorrão de salsicha			11,50')
print('105		xTudo							18,00')
print('----------------------------------------------')

while True:

	codigo = int(input("Informe o código Produto ou ZERO para sair: "))

	if codigo == 0:
		break
	elif codigo >= 100 and codigo <= 105:
		qtde = int(input("Informe a quantidade: "))

		valorTotal = 0

		if codigo == 100:
			valorTotal = qtde * 5
		elif codigo == 101:
			valorTotal = qtde * 12
		elif codigo == 102:
			valorTotal = qtde * 14.5
		elif codigo == 103:
			valorTotal = qtde * 16
		elif codigo == 104:
			valorTotal = qtde * 11.5
		elif codigo == 105:
			valorTotal = qtde * 18

		print(f"Valor total do item é R$ {valorTotal:<12.2f}")
		print("-" * 50)

		totalPedido += valorTotal

	else:
		print(">>> o Código informado do item é inválido <<<")

#
print("=" * 50)
print(f"Valor total do pedido R$ {totalPedido:<12.2f}")
print("=" * 50)