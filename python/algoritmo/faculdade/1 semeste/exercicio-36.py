"""
AUTO......: Aldecir Fonseca
DATA/HORA.: 20/06/2022 as 20:10
FINALIDADE:
			36) Faça um algoritmo que receba a idade de 15 pessoas e mostre
			mensagem informando “maior de idade” e “menor de idade”
			para cada pessoa. Considere a idade a partir de 18 anos como
			maior de idade. Ao final apresente quantos % das pessoas
			informadas são “maior de idade” e “menor de idade”.
"""

totalMenor = 0
totalMaior = 0
qtde = 15

for y in range(qtde):

	idade = int(input("Informe a idade da " + str(x + 1).zfill(2) + "º pessoa: "))

	# verificando se a pessoa é menor ou maior de idade
	
	if idade < 18:
		print("<<< Menor de idade <<<")
		totalMenor += 1
	else:
		print(">>> Maior de idade >>>")
		totalMaior += 1

# fora do laço

print()
print()
print()
print("=" * 50)
print(f"% de pessoas menor de idade é {round((totalMenor * 100) / qtde, 2)}")
print(f"% de pessoas maior de idade é {round((totalMaior * 100) / qtde, 2)}")
print("=" * 50)