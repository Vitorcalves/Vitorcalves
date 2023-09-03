a = []

print("_" * 30)
print("ordencao de valores com metodo bolha")
print("_" * 30)

for x in range(5):
    a.append(int(input("informe um valor: ")))



for x in range(1, len(a)):
    for y in range(len(a) - 1, 0, -1):
        if a[y] < a[y - 1]:
            aux = a[y]
            a[y] = a[y - 1]
            a[y - 1] = aux

print("-" * 30)
print(a)