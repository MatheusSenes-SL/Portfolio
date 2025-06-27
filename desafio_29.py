import math
veloc = int(input("Velocidade: "))
veloc_max = int(input("Velocidade Máxima: "))
multa1 = int(veloc_max - veloc)
# print(multa1) -- Use esse print para descobrir o resultado, mas não os deixe na hora final.
multa2 = ((math.sqrt(math.pow(multa1, 2)))*7)
# print(multa2) -- Use esse print para descobrir o resultado, mas não os deixe na hora final.
if veloc <= veloc_max:
    print("Você está de acordo com a lei.")
else:
    print("Você ultrapassou o limite de velocidade que era de {}km/h.".format(veloc_max))
    print("Como sua velocidade era de {}, sua multa será de {:2f}".format(veloc, multa2))
print("end")
