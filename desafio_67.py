a = cont = mult = 0
print(f"{'=' * 45}\nDigite um número positivo para ver sua tabuada\n um negativo para fechar o programa.\n{'=' * 45}")
while True:
    a = int(input("Digite um número: "))
    print('~=~' * 15)
    if a < 0:
        break
    else:
        while cont < 10:
            cont += 1
            mult = a * cont
            print(f"{a} x {cont} = {mult}")
            print('~=~' * 15)
print('=' * 45)
print("Agradecemos pela preferência!")
print('=' * 45)
