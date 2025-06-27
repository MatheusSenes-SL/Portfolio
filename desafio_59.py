# -------------------------------VALORES REQUISITADOS-------------------------------
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
sm = 1
mult = 2
maior = 3
novo = 4
div = 5
sair = 6
iniciar = ""
decide = ""
# ------------------------------------PROGRAMA--------------------------------------
while decide != 6:

    print("""Digite:
    [1] Somar (Some os dois números)
    [2] Multiplicar (Multiplique os dois números)
    [3] Maior (Compare e verifique qual dos dois números é o maior)
    [4] Novos Números (Escolha novos valores para os números)
    [5] Dividir (Faça uma divisão na ordem dita dos números)
    [6] Sair (Feche o programa)""")
    decide = int(input("O que pretende fazer? "))
    if decide == sm:
        print("{}".format("=" * 20))
        print("A soma entre {} e {} é {}".format(v1, v2, (v1 + v2)))
        print("{}".format("=" * 20))
    elif decide == mult:
        print("{}".format("=" * 20))
        print("Ao multiplicar {} por {}, temos {}".format(v1, v2, (v1 * v2)))
        print("{}".format("=" * 20))
    elif decide == maior:
        print("{}".format("=" * 20))
        if v2 > v1:
            print("O número {} é maior do que o {}.".format(v2, v1))
        elif v1 > v2:
            print("O número {} é maior do que o {}.".format(v1, v2))
        else:
            print("Os números são iguais.")
        print("{}".format("=" * 20))
    elif decide == novo:
        v1 = int(input("Digite um valor novo: "))
        v2 = int(input("Digite um segundo valor novo: "))
    elif decide == div:
        print("{}".format("=" * 20))
        print("{:.4f} é o resultado mais próximo do resultado de {} dividido pelo quociente {}".format(float(v1 / v2), v1, v2).replace(".", ",") + ".")
        print("{}".format("=" * 20))
    else:
        print("Comando inválido. Tente novamente.")
print("Programa finalizado.")
