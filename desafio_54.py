import datetime
ano = datetime.date.today().year
print(ano)
age = 0
novo = 0
adulto = 0
velho = 0
for i in range(0, 6):
    nasceu = int(input("Digite o ano em que nasceu: "))
    age = ano - nasceu
#    novo += 1
#    adulto += 1
#    velho += 1
    if 0 <= age <= 18:
        print("Idade:\033[34m{}\033[m".format(age))
        novo += 1
        print(novo)
    elif 18 < age < 60:
        print("Idade:\033[33m{}\033[m".format(age))
        adulto += 1
        print(adulto)
    elif 130 > age >= 60:
        print("Idade:\033[35m{}\033[m".format(age))
        velho += 1
        print(velho)
    elif age < 0:
        print("\033[31mHouve algum erro. Por favor, ponha uma idade acima de 2 meses.\033[m")
    elif age >= 130:
        print("\033[31mHouve algum erro? Parece que sua idade é maior do que a expectativa de vida até o ano de 2023...\033[m")
print("Nessa lista temos: \n{} jovem(ns);\n{} adulto(s);\n{} idoso(s);".format(novo, adulto, velho))