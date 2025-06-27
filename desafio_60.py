# ------------------------------------------MÉTODO ORIGINAL-----------------------------------------------------
from math import factorial
key = ""
print("""programa 1 (Feito por mim)
""")
while key != "N":
    num = int(input("Digite um número para saber sua fatorial: "))
    print("A fatorial de {} é {}.".format(num, factorial(num)))
    key = str(input("Quer continuar com o programa[S/N]? ")).strip().upper()[0]
print("Programa finalizado. Obrigado pela preferência!")
# ------------------------------------------MÉTODO REQUERIDO--------------------------------------------------
print("""
Programa 2 (requisitado pelo professor)""")

num = int(input("Digite um número para saber sua fatorial: "))
n = num
while n >= 1:
    print(' {} x'.format(n), end='')
    n -= 1
print(" 0 = {}".format(factorial(num)))
print("end")
#---------------------------------------------DESAFIO EXTRA-------------------------------------------------------
print("""
Programa 3 (Desafio extra proposto pelo professor)""")
num = int(input("Digite um número para saber sua fatorial: "))
n = num
f = 1
for n in range(num, 0, -1):
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print('{}'.format(f))