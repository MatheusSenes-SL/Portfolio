import random
n1 = str(input("Aluno um: "))
n2 = str(input("Aluno dois: "))
n3 = str(input("Aluno tres: "))
n4 = str(input('Aluno quatro: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("Agora a lista é: {}".format(lista))
