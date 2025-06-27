cidade = str(input("Digite a cidade em que nasceu: ")).strip()
ci = (cidade.split())
print(("Santo" in ci[0]) or ("Santa" in ci[0]))

# OBS:
# 'or' ainda não foi apresentado, mas eu imaginei que seria utilizado assim. Verificarei nas aulas posteriores.
# O código pode ser inválido se utilizar em minúsculo, por exemplo. Então podemos adicionar o '.upper' para aprimorá-lo.
ciu = (cidade.upper())
CI = (ciu.split())
print(("SANTO" in CI[0]) or ("SANTA" in CI[0]))

# Você também pode finalizar assim, utilizando == que é para comparação:
print((CI[0] == "SANTO") or (CI[0] == "SANTA"))
