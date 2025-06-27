#-=-=-=-=-=-=-=-=-=-==-=-=-=-=-Variáveis=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
sexo = idade = icont = cont = hcont = mcont = 0
ans = ""
#=-=-=-=-=-=-=-=-=--=-=-=Início do Programa-=-=-=-=-=-=-=-=-=-=-=-=-=-
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: ")).strip().upper()
    cont += 1

    if idade >= 18:
        icont += 1
    if idade < 20 and sexo[0] == "F":
        mcont += 1
    if sexo == "M":
        hcont += 1
    while True:
        ans = str(input("Deseja continuar? ")).strip().upper()
        if ans[0] == "S":
            break
        if ans[0] == "N":
            break
    if ans == "N":
        break
print(f"""Resultados do cadastro com {cont} pessoas:
{icont} pessoa(s) maior(es) de idade.
{mcont} mulher(es) com idade abaixo de 20 anos.
{hcont} homem(ns) participaram deste cadastro.""")