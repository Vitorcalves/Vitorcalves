altura = float(input("insira a sua altura "))
sexo = input("insira m se a pessoa for do sexo masculino e f se for do feminino ")
if sexo != "m" and sexo != "f" :
    print("sexo invalido")
elif sexo == "m" :
    print("seu peso ideal e ",(62.1 * altura) - 58)
else:
    print("seu peso ideal e ",(72.7 * altura) - 44.7)