continuar = ""
n = 0
num1 = int(input("Digite o primeiro termo da P.A.: "))
raz = int(input("Digite a razão da P.A.: "))
ult = int(input("Digite a posição do último termo da P.A.: "))
s = num1
while continuar != 1:
    while n < ult:
        n += 1
        s *= raz
        print("{}".format(s), end="")
        print("{}".format("->") if n < ult else "", end="")
    print("")
    continuar = int(input("""[0] Adicionar mais números\n[1] Sair
Digite a opção que quer: """))
    if continuar == 0:
        add = int(input("Quantas posições a mais você quer adicionar? "))
        ult += add
    elif continuar == 1:
        print("Tudo bem. Agradecemos pela preferência!")
    else:
        print("Não foi possível identificar o seu comando. Poderia repeti-lo?")
