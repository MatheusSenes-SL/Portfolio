import time
# Valores
poup = acc = valor = ans = dep = add = grab = float(0)
ccount = count = vcount = dcount = ucount = cecount = 0
cin = 50
vin = 20
dez = 10
um = 1
cent = 0.01
# Programa
while True:
    time.sleep(1)
    print("~=-=~" * 11)
    ans = int(input("""Bem vindo à sua poupança! O que deseja fazer?
    [0] Ver poupança atual.
    [1] Depositar dinheiro.
    [2] Sacar dinheiro.
    [3] Sair de sua conta.
Digite o número da opção desejada para realizá-la: """))
    time.sleep(1)
    if ans == 0:
        print("-=-=-" * 11)
        print(f"Saldo atual guardado: R${poup}")
    if ans == 1:
        print("^=-=^" * 11)
        print(f"Saldo atual: R${poup}")
        dep = float(input("Digite a quantia que deseja depositar: R$"))
        if dep < 0:
            print("**=**" * 11)
            print("não foi possível adicionar esta quantia.")
        else:
            print("-===-" * 11)
            poup += dep
            print("Depósito realizado com sucesso!")
            print(f"Agora você tem R${poup} em sua poupança.")
    if ans == 2:  # Saque
        print("-=*=-" * 11)
        print(f"Saldo atual: R${poup}")
        grab = float(input("Digite a quantia que deseja sacar: R$"))
        a = grab
        while True:
            while a >= cin:
                a -= cin
                ccount += 1
            while a >= vin:
                a -= vin
                vcount += 1
            while a >= dez:
                a -= dez
                dcount += 1
            while a >= um:
                a -= um
                ucount += 1
            while a >= cent:
                a -= cent
                cecount += 1
            break
        if grab > poup:
            acc = str(input(f"Caso saque este valor, sua poupança será negativada. Deseja continuar? ")).strip().upper()
            if acc[0] == "S":
                poup -= grab
                if poup > 0:
                    print(f"Agora você tem R${poup} em sua poupança.")
                else:
                    print(f"Sua poupança está negativada. Você tem R${poup}.")
                print("Você deve receber:")
                if cin > 0:
                    print(f"{ccount} notas de 50;")
                if vin > 0:
                    print(f"{vcount} notas de 20;")
                if dez > 0:
                    print(f"{dcount} notas de 10;")
                if um > 0:
                    print(f"{ucount} moedas de 1;")
                if cent > 0:
                    print(f"{cecount} centavos.")
            else:
                print(f"Saque negado. Saldo atual: {poup}")
        elif grab <= poup:
            poup -= grab
            print("Você deve receber:")
            if cin > 0:
                print(f"{ccount} notas de 50;")
            if vin > 0:
                print(f"{vcount} notas de 20;")
            if dez > 0:
                print(f"{dcount} notas de 10;")
            if um > 0:
                print(f"{ucount} moedas de 1;")
            if cent > 0:
                print(f"{cecount} centavos.")
            ccount = vcount = dcount = cecount = ucount = 0
            print(f"Agora você tem R${poup} em sua poupança.")
    if ans == 3:
        break
    if ans > 3 or ans < 0:
        print("Comando desconhecido. Por favor, tente novamente.")
print("Você deve receber:")
print("Programa finalizado. Muito obrigado pela preferência!")
