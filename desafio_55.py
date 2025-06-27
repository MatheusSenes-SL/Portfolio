ordem = 0
menor = 0
maior = 0
for kg in range(1, 6):
    peso = float(input("Digite o {}° peso: ".format(kg)))
    if kg == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O menor peso da lista é {}Kg".format(menor).replace(".", ",") + ".")
print("O maior peso da lista é {}Kg".format(maior).replace(".", ",") + ".")

#