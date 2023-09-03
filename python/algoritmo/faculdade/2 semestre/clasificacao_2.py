nome = []
idade = []

print("_" * 30)
print("orrdenacao dos valores com metodo bolha")
print("_" * 30)


for x in range(5):
    nome.append(input("informe seu nome: "))
    idade.append(int(input("inome sua idade: ")))

for x in range(1, len(idade)):
    for y in range(len(idade) -1, 0, -1):