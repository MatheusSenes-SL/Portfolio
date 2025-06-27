# ------------------------------DADOS NECESSÁRIOS-----------------------------------
quant = 0

# pessoas
pes = 0
p1 = 0
p2 = 0
p3 = 0
# valores
idade = 0
sexo = ""
# nome
n1 = ""
n2 = ""
n3 = ""
# sexo
s1 = ""
s2 = ""
s3 = ""
# idade
i1 = 0
i2 = 0
i3 = 0
maior = 0
qmul = 0
# ---------------------------------------INÍCIO-------------------------------------
for pes in range(1, 4):
    quant = pes
    print("{}PESSOA{}{}".format(10 * "=", pes, 10 * "="))
    nome = str(input("Digite o {}° nome: ".format(pes))).strip().title()
    idade = int(input("Digite a {}° idade: ".format(pes)))
    sexo = str(input("Digite o sexo da pessoa[M/F]: ")).strip().upper()
    if pes == 1:
        p1 = pes
        n1 = nome
        i1 = idade
        maior = i1
        if sexo == "M":
            s1 = "M"
        elif sexo == "F":
            s1 = "F"
    if pes == 2:
        n2 = nome
        p2 = pes
        i2 = idade
        if idade > maior:
            maior = i2
        if sexo == "M":
            s2 = "M"
        elif sexo == "F":
            s2 = "F"
    if pes == 3:
        n3 = nome
        p3 = pes
        i3 = idade
        if idade > maior:
            maior = i3
        if sexo == "M":
            s3 = "M"
        elif sexo == "F":
            s3 = "F"


# ---------------------------------HOMEM MAIS VELHO---------------------------------
if p1 and (s1 == "M") and maior:
    print("{} é o homem mais velho, sendo sua idade {}.".format(n1, maior))
#    print(s1 == "M")
elif p2 and (s2 == "M") and maior:
    print("{} é o homem mais velho, sendo sua idade {}.".format(n2, maior))
#    print(s2 == "M")
elif p3 and (s3 == "M") and maior:
    print("{} é o homem mais velho, sendo sua idade {}.".format(n3, maior))
#    print(s3 == "M")
else:
    print("Não há homens nesta lista.")

# -----------------------------MÉDIA ARITMÉTICA DE IDADES---------------------------
media = (i1 + i2 + i3) / quant
print("A média entre as {} idades registradas é {}".format(quant, media))

# -----------------------------MULHERES MENORES DE VINTE----------------------------
if p1 and s1 == "F":
    if i1 < 20:
        qmul = qmul + 1
if p2 and s2 == "F":
    if i2 < 20:
        qmul = qmul + 1
if p3 and s3 == "F":
    if i3 < 20:
        qmul = qmul + 1
print("Há {} mulheres com idade menor que 20 anos.".format(qmul))

#------------------------CHECAGEM-------------------------------------------------
#print(p1, p2, p3,)  # pessoas
#print(i1, i2, i3)
#print(media)  # media aritmetica das idades
#print(quant)  # quantidade
#print(maior)  # maior idade
#print(s1, s2, s3)  # sexo
