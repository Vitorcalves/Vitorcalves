"""
-------------------------------------------------
DATA/HORA..: 14/06/2022 às 19:28
ESCRITO POR: Aldecir Fonseca
FINALIDADE.: 33) Faça um algoritmo que determine o maior 
                entre N números lidos. 
                - A condição de parada é a entrada de um valor 0.
                - Ou seja, o algoritmo deve ficar calculando 
                    o maior até que a entrada seja igual a 0 (ZERO).
-------------------------------------------------
"""

maior = 0

while True:
    valor = int(input("Informe um valor (ou ZERO para sair): "))

    if valor == 0:
        break
    else:
        if valor > maior:
            maior = valor

# fora do laço

print("=" * 50)
print(f"O maior valor informado foi {maior}")
print("=" * 50)