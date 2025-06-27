num = int(input("Digite um número para verificar se ele é primo: "))
tot = 0
print("O que estiver em azul registra os divisores deste número:")
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[34m", end='')
        tot += 1
    else:
        print("\033[31m", end='')
    print(" {};".format(c))
print("\033[mO número {} foi dividido {} vezes".format(num, tot))
if tot == 2:
    print("Logo {} é um número primo.".format(num))
else:
    print("Logo {} é um número comum.".format(num))
