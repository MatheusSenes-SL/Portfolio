a = s = cont = 0
while True:
    a = int(input("Digite um número: "))
    if a == 999:
        break
    s += a
    cont += 1
print(f'A soma dos {cont} números digitados é {s}')
