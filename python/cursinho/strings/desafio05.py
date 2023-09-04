frase = 'ola bem-vindo ao treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
print(frase.split('o', 2)) #separa a string em 3 partes
lista = frase.split('o', 2)
print('O'.join(lista)) #junta a string com o caracter
