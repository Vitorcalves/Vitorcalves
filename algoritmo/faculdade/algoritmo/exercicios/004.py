# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


from re import I


a = int(input("insira a populacao da primeira cidade "))
b = int(input("insira a populacao da segunda cidade "))
pa = float(input("insira a porcentagem de crecimento da primeira cidade "))
pb = float(input("insira a porcentagem de crecimento da segunda cidade "))
cont = 0
if a > b:
    maior = "A"
else:
    maior = "B"
if pa > pb:
    maiorp = "PA"
else:
    maiorp = "PB"
if maior == maiorp:
    print("nunca teram a mesma populacao")
elif maior == "A":
    while a > b:
        b = b + b * (pa / 100)
        a = a + a * (pb / 100)
        cont += 1
    print(f"habitantes de A ",a ," e de B ",b ," total de anos {cont}")
elif maior == "B":
    while a < b:
        b = b + b * (pa / 100)
        a = a + a * (pb / 100)
        cont += 1
    print(f"habitantes de A ",a ," e de B ",b ," total de anos {cont}")