#exemplo 1
# coding : utf-8

"""
data/hora : 31/05/2022 ás 18:48
copiado por Vitor Cunha Alves
"""

p1 = float(input("informe nota da prova 1: "))
p2 = float(input("informe nota da prova 2: "))
p3 = float(input("informe nota da prova 3: "))
p4 = float(input("informe nota da prova 4: "))

media = (p1 + p2 + p3 + p4) / 4 #calcula media do aluno

print ("a media do aluno é " + str(media))

if media < 2:
    print("aluno foi reprovado")
elif media > 2 and media < 5 or media == 5:
    print("aluno em recuperação")
    notarecuperacao = float(input("informe a nota da prova de recuperação"))

    media = (media + notarecuperacao) / 2

    if media >=5:
        print("aluno aprovado em prova de recuperação com media", media)
    else:
        print("aluno reprovado em prova de recuperação com media", media)
else:
    print("aluno esta aprovado")