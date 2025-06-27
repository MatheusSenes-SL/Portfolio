idade = int(input("Qual a sua idade? "))
if idade <= 9:
    print("\033[1;32mVocê é um nadador do nível MIRIM")
elif 9 < idade <= 14:
    print("033[1;31mVocê é um nadador do nível INFANTIL")
elif 14 < idade <= 19:
    print("\033[1;33mVocê é um nadador do nível JÚNIOR")
elif 19 < idade <= 20:
    print("\033[1;34mVocê é um nadador do nível SÊNIOR")
else:
    print("\033[1;35mVocê é um nadador do mais alto nível MASTER! \033[m")