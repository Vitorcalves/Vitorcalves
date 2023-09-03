fat = 1
n = int(input("digite um valor"))

for a in range(2, n + 1):
    fat = fat * a

print(f' o fatorial de {n} e {fat}')