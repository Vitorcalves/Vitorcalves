eixo = int(input("insira a qunatidade de eixos "))
if eixo < 2:
    print("quantidade de eixos inferior ao suportado")
else :
    if eixo > 9 :
        print("quantidade de eixos superior ao suportado")
    else :
        placa = input("insira a placa do veiculo ")
        print("o valor do pedagio do veiculo de placa", placa ," e de ",eixo * 6.35 , "r$")