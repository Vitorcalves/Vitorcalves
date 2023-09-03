"""
AUTO......: Aldecir Fonseca
DATA/HORA.: 20/06/2022 as 21:19
FINALIDADE:
			35) Ler 20 números e ao final informar quantos número(s) est(á)ão
			no intervalo entre 10 (inclusive) e 50 (inclusive).
"""

qtdeIntervalo = 0;

for x in range(20):
	numero = int(input("Informe " + str(x + 1).zfill(2) + " valor: "))

	if numero >= 10 and numero <= 50:
		qtdeIntervalo += 1;

# fora do laço

print("=" * 50)
print(f"Você digitou {qtdeIntervalo} no intervalo entre (10 à 50), inclusive")
print("=" * 50)