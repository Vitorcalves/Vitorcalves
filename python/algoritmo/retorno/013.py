salario = float(input('Insira o valor de salario do funcinario R$'))
porcento = int(input('Insira o valor de aumento que sera aplicado '))

nsalario = salario + (salario * porcento / 100)

print(f'O colaborador que ganhava R${salario :.2F} com o aumento de {porcento}% passou a receber R${nsalario :.2f}')