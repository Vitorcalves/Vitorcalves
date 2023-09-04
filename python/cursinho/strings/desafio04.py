teclado = 'Teclado'
print(teclado[-1])
print(teclado.index('l'))
print(teclado[teclado.index('l')])
# acessando partes da string
link = 'facebook.com/usuario'
print(link[0:])
print(link[-1])
print(link[0:5])
print(link[1:])
print(link[-5:])
print(link[0:5:2])
print(link[0::2])
# acessando partes da string por fatiamento 0 e onde se inidicia e vai ate o final com passo 2
frase = 'clean clean'
print(frase.rindex('c'))

# desafio 04
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

# desafio 05
aplicacao = 'desenvolvimento de aplicacao'
print(f" {aplicacao[-12].upper()}{aplicacao[-11:]}")