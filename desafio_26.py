frase = str(input("digite uma frase, que eu lhe direi fatos sobre a letra A:  ")).strip()
quant = frase.upper()
print("A sua frase é".format(frase))
print("""Ela tem {} letras. A letra "A" aparece {} vezes.
Aparece pela primeira vez no {}° dígito.
E pela última vez pelo {}° dígito.""".format((len(quant) - 1), quant.count("A"), quant.find("A")+1, quant.rfind("A", 10, 20)+1))

# OBS:
# Você pode usar "rfind" para procurar a partir da direita e imagino que alguns outros podem ter isso também.
# Não é preciso fazer mais uma variável. Tem como por depois do ".strip()" o "upper()".
