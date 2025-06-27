valor = int(input("Digite o seu salário: "))
mai = ((valor + (valor * 10)) / 100)
men = ((valor + (valor * 15)) / 100)
if valor > 1250:
    print("Seu novo salário será de {}.".format(float(mai)))
else:
    print("Seu novo salário será de {}.".format(float(men)))
print("end")