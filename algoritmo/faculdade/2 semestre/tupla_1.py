# Crie uma tupla com os valores referente aos meses do ano preenchidos por extenso. Seu programa deverá pedir ao usuário para informar o mês desejado e imprimir na tela o mês por extenso pegando a descrição na tupla criada. Se o usuárioinformar um mês inválido, dar uma mensagem e pedir parainformar novamente o mês. 

mes = ['1', 'janeiro', 'fevereiro', 'marco', 'abil', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'desembro']

while True:
    numero = int(input("escreva o numero do mes desejado "))

    if numero < 1 or numero > 12:
        print("mes invalido")
    else:
        break

print("o mes escolhido foi ",mes[numero])