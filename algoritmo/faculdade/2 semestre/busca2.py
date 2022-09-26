nome = []
idade = []

while True:
    print("-" * 30)
    print("MENU DE OPÇÕES")
    print()
    print("1) Cadastrar pessoas")
    print("2) Exibir em ordem crescente de nome")
    print("3) Exibir em ordem decrescente de idede")
    print("4) Sair")
    print("-" * 25)
    opc = int(input("informe a opção desejada: "))

    if opc == 1:
        print()
        print("#" * 30)
        print(f"informe os dados para a pessoa{len(nome)}")

        nome.append(input("nome: "))
        idade.append(int(input("idade: ")))

    elif opc == 2:
        for x in range(1, len(nome)):
            for y in range(len(nome) -1, )
    