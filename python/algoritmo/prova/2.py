numeros = []
soma = 0 
media = 1  
par = 9999999999999999999999  
menor = 0
for x in range(10):
    
    numero = int(input("insira um numero inteito com ate 20 algarismos "))
    while True:
        if numero > 99999999999999999999:
            numero = int(input("numero invalido insira um numero inteito com ate 20 algarismos "))
        else:
            break
    numeros.append(numero) 
    if numeros[x] == 0:
        menor = 0

    else:
        if numeros[x] < numeros[menor]:
            menor = x
    if (numeros[x] % 2 ) == 0:
        if numeros[par] > numeros[x]:
            par = x
    else:
        par = -1
    media = media + numero
    soma = soma + numero
media = media / 10

print(f"a soma dos valores e {soma} ")

print("a media dos valores e de ",media )


print(f"O menor numero e {numeros[menor]} e seu indice e {menor}")
if par == -1:
    print("nao tem numeros pares")
else:
    print(f"o indice do menor valor par e {par}")
