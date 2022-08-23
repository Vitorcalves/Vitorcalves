nome = []
altura = []
menor = 0
maior = 0

for x in range(11):
    nome.append(input("insira o nome do jogador "))
    altura.append(float(input("insira a altura do jogador ")))
    if x == 0:
        menor = x
        maior = x
    else:
        if menor > altura[x]:
            menor = x
        if maior < altura[x]:
            maior = x
for x in range(len(nome)):
    print(f"jogador {nome[x]}")
    print(f"altura{altura[x]}")
print(f"{nome[maior]} e o jogado mais alto do time com {altura[maior]}")
print(f"{nome[menor]} e o menor jogador do time com {altura[menor]} e esta no indice {menor}")