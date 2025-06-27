num = 0
a = 0
cont = 0
s = ""
maior = 0
menor = 0
while s != "N":
    num = int(input("Digite um número: "))
    s = str(input("Digite se quer continuar [S/N]: ")).strip().upper()
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    a += num
media = a / cont
print("A média dos {} números digitados é {}.".format(cont, media))
print("O maior número entre eles é o {}, enquanto o menor é o {}.".format(maior, menor))
