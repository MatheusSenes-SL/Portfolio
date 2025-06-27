num1 = int(input("Digite o primeiro termo da P.A.: "))
raz = int(input("Digite a razão da P.A.: "))
ult = int(input("Digite a posição do último termo da P.A.: "))
n = 0
s = num1
while n < ult:
    n += 1
    s += raz
    print("{}".format(s), end="")
    print("{}".format("->") if n < ult else "", end="")

# Eu estava pensando em uma coisa e... realmente... preciso deixar meus códigos mais limpos e mais fáceis
# de entender para outros programadores. Imagina se eu me torno um SamirDEV da vida?
