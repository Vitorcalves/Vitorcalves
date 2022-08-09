piloto = ["carinha", "outro", "popo", "weversom", "emo", "surfista", "joerlei", "cleberson", "garson", "intruso", "K.Raikkonen", "outro intruso", "popo2.0", "bot1", "bot2", "bot3", "bot4", "bot5", "bot6", "bot7"]

print(piloto)
print("primeiro colocado",piloto[0])
print("segundo colocado",piloto[1])
print("terceiro colocado",piloto[2])

for posicao, nome in enumerate(piloto):
    print(f"{posicao + 1:>2.0f} - {nome}")

print("ters primeiros colocados")

for n in range(0, 3):
    print(f"{n + 1:>2.0f} - pilotos[n]")

for n in range(len(piloto) - 4, len(piloto)):
    print(f"{n + 1:>2.0f} - {piloto[n]}")

print("carinha esta localizado em")

for n in range(len(piloto)):
    if piloto[n] == "carinha":
        print(f"o indice esta localizado e {n}")



