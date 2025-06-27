viagem = int(input("Digite a distância que será percorrida: "))
men200 = float(viagem * 0.50)
mai200 = float(viagem * 0.45)
if viagem <= 200:
    print("o custo de sua viagem foi de {}".format(men200))
else:
    print("o custo de sua viagem foi de {}".format(mai200))
print("end")
