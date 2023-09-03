"""
-------------------------------------------------
DATA/HORA..: 14/06/2022 às 19:49
ESCRITO POR: Aldecir Fonseca
FINALIDADE.: 34) Leia 10 valores inteiros e determine:  
                    - Qual é o menor valor informado;
                    - Qual é o maior valor informado;
                    - A soma dos valores informados;
                    - A média dos valores informados.
-------------------------------------------------
"""

menor = 0
maior = 0
soma  = 0

for x in range(10):
    valor = int(input("Informe o valor " + str(x + 1) + ": "))

    if x == 0:
        menor = valor
        maior = valor
    else:
        # apurar menor valor
        if valor < menor:
            menor = valor

        # apurar maior valor
        if valor > maior:
            maior = valor

    soma += valor

#

print("=" * 50)
print(f"Menor valor encontrado é {menor}")
print(f"Maior valor encontrado é {maior}")
print(f"A soma dos valores informados é {soma}")
print(f"A média dos valores informados é {(soma / 10):<12.2f}")
print("=" * 50)