import random
um = input("Aluno 1: ")
dois = input("Aluno 2: ")
tres = input("Aluno 3: ")
quatro = input("Aluno 4: ")
lista = [um, dois, tres, quatro]
escolhido = random.choice(lista)
print("vem apagar o quadro {}!".format(escolhido))

