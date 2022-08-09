"""
-------------------------------------------------
DATA/HORA..: 13/06/2022 às 20:22
ESCRITO POR: Aldecir Fonseca
FINALIDADE.: 32) Desenvolva um algoritmo que solicite ao usuário que 
                informe o nome, sexo e idade de 10 alunos. No final 
                apresente:

                - O nome do aluno mais novo.
                - O nome do aluno mais velho do sexo Masculino.
                - A média de idade das alunas.
-------------------------------------------------
"""

cont            = 1

alunoNovoNome   = ""
alunoNovoIdade  = 0

alunoVelhoNome  = ""
alunoVelhoIdade = 0

somaIdadeAlunas = 0
qtdeAlunas      = 0

while cont <= 5:

    print(f"Informe os dados do aluno {cont}")
    print("-" * 50)
    nome    = input("Nome..........................: ")
    idade   = int(input("Idade.........................: "))

    while True:
        sexo    = input("Sexo (M=Masculino; F=Feminino): ")

        if sexo.upper() == "M" or sexo.upper() == "F":
            break
        else:
            print("Sexo inválido")

    # Apurando aluno mais novo

    if idade < alunoNovoIdade or cont == 1:
        alunoNovoNome   = nome
        alunoNovoIdade  = idade

    # Aluno mais velho sexo masculino

    if sexo.upper() == "M":
        if idade > alunoVelhoIdade:
            alunoVelhoNome  = nome
            alunoVelhoIdade = idade
    else:   # Média de idade das alunas
        somaIdadeAlunas += idade
        qtdeAlunas      += 1

    cont += 1

# exibindo apuração dos dados
print("=" * 50)
print(f"Aluno mais novo é {alunoNovoNome} e tem {alunoNovoIdade} ano(s)")
print(f"O Aluno mais velho do sexo masculino é {alunoVelhoNome} e tem {alunoVelhoIdade} ano(s)")
print(f"A média de idade das alunas é {(somaIdadeAlunas / qtdeAlunas):<3.0f}") 
print("=" * 50)