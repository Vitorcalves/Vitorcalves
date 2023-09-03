# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("insira seu nome e ele deve conter no minimo 4 caracteres ")
    if len(nome) < 4:
        print("nome invalido")
    else:
        break

while True:
    idade = int(input("insira uma idade entre 0 e 150 "))

    if (idade < 0) or (idade > 150):
        print("idade invalida")
    else:
        break
            
while True:
    salario = int(input("insira o seu salario "))
    if salario < 1:
        print("salario invalido")
    else:
        break

while True:
    sexo = input("Sexo (M=Masculino; F=Feminino): ")

    if sexo.upper() == "M" or sexo.upper() == "F":
        break
    else:
        print("Sexo inválido, informe um sexo válido para continuar")

while True:
    civil = input("insira seu estado civil (use S para solteiro, C casado, V para viuvo, D para divorciado) ")

    if ( civil.upper() == "S") or (civil.upper() == "C") or (civil.upper() == "V") or (civil.upper() == "D"):
        break
    else:
        print("estado civil invalido")

