"""

"""
valores = []
for i in range(10):
    valores.append(int(input("digite um valor: ")))

for x in range(1, len(valores)):
    for y in range(len(valores) - 1, 0, -1):
        if valores[ y ] > valores[y - 1]:
            aux = valores[y]
            valores[y] = valores[y - 1]
            valores[y - 1] = aux

print("=" * 20)
print("lista de valores em ordem crecente")
print("=" * 20)

for x in range(len(valores)):
    print(f"{valores[x]}")
