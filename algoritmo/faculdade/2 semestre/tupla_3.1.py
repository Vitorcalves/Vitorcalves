piloto = ["carinha", "outro", "popo", "weversom", "emo", "surfista", "joerlei", "cleberson", "garson", "intruso" ,"K.Raikkonen", "outro intruso", "popo2.0", "bot1", "bot2", "bot3", "bot4", "bot5", "bot6", "bot7"]

print(piloto)
print("primeiro colocado",piloto[0])
print("segundo colocado",piloto[1])
print("terceiro colocado",piloto[2])

for posicao, nome in enumerate(piloto):
    print(f"{posicao + 1:>2.0f} - {nome}")

print("ters primeiros colocados")

for n in range(0, 3):
# for n in range(3):

    print(f"{n + 1:>2.0f} - {piloto[n]}")

for n in range(len(piloto) - 4, len(piloto)):
    print(f"{n + 1:>2.0f} - {piloto[n]}")

print("carinha esta localizado em")

busca = input("informe o piloto desejado:")

achou = False

for n in range(len(piloto)):
    if piloto[n]. upper() == busca.upper():
        print(f"piloto {busca} esta localizado em {n + 1:>2.0f} ")
        achou = True

if not achou:
    print("o piloto nao foi localizado")



# for n in range(len(piloto)):
#     if piloto[n] == "K.Raikkonen":
#         print(f"o piloto esta localizado em {n} no indice")



