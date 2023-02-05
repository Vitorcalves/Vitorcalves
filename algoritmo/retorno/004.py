def consulta (tipe, nome):
    if tipe:
        print(f'Você digitou {nome}')


valor = input('Digite algo ')
print(f'O tipo primitivo desse valor é {type(valor)}')

consulta(valor.isspace(),'espaços')

consulta(valor.isnumeric(), 'numeros')

consulta(valor.isalpha(), 'alfabetico')

consulta(valor.isalnum(), 'alfanumerico')

consulta(valor.isupper(), 'em maiusculo')

consulta(valor.islower(), 'em minusculo')

consulta(valor.istitle(), 'termo capitalizado')
