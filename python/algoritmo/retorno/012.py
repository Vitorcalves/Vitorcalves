desconto = int(input('Insira o valor do desconto '))
produto = float(input('Insira o valor do produto R$'))
final = produto - (produto * desconto / 100)
print(f'o valor do produto com o desconto de {desconto}% e de R${final :.2f}')