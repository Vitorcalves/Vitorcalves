"""
-------------------------------------------------
DATA/HORA..: 13/06/2022 às 20:22
ESCRITO POR: Aldecir Fonseca
FINALIDADE.: 31) Solicite o Salário Bruto de um funcionário. 
                Considere como valor do salário mínimo: R$ 998,00. Calcule e exiba o 
                salário liquido descontando o imposto de renda conforme tabela abaixo. 
                Formula: Salário Liquido ← Salário Bruto – Imposto de Renda. 
                Os valores da alíquota para cálculo do imposto de renda são

                Salário Bruto               Alíquota
                -------------------------------------
                Até 2 salários mínimos      Isento
                2 a 3 salários mínimos      7,5%
                3 a 5 salários mínimos      15%
                5 a 7 salários mínimos      22,5%
                Acima de 7 sal. mínimos     30%
-------------------------------------------------
"""

salarioBruto    = float(input("Informe o salário Bruto: "))
salarioMinimo   = 998
salarioLiquido  = 0
descImpRenda    = 0

if salarioBruto <= (salarioMinimo * 2):
    descImpRenda = 0
elif salarioBruto <= (salarioMinimo * 3):
    descImpRenda = (salarioBruto * 7.5) / 100
elif salarioBruto <= (salarioMinimo * 5):
    descImpRenda = (salarioBruto * 15) / 100
elif salarioBruto <= (salarioMinimo * 7):
    descImpRenda = (salarioBruto * 22.5) / 100
else:
    descImpRenda = (salarioBruto * 30) / 100

salarioLiquido = salarioBruto - descImpRenda

print("=" * 37)
print(f"Salário Bruto...... R$ {salarioBruto:>14.2f}")
print(f"Desconto Imp.Renda. R$ {descImpRenda:>14.2f}")
print(f"Salário Líquido.... R$ {salarioLiquido:>14.2f}")
print("=" * 37)