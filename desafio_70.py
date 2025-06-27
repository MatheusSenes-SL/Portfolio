#Variaveis
barato = bnome = total = nome = valor = ans = count = bcount = 0
#Programa
while True:
    nome = str(input("Nome do produto: "))
    valor = float(input("Valor do produto: "))
    count += 1
    total += valor
    if count == 1:
        barato = valor
        bnome = nome
    if barato < valor:
        barato = valor
        bnome = nome
    if valor > 1000:
        bcount += 1
    while True:
        ans = str(input("Quer continuar?[S/N]")).strip().upper()
        if ans[0] == "S":
            break
        if ans[0] == "N":
            break
    if ans[0] == "N":
        break

print(f"""As suas compras tiveram um resultado interessante:
Você gastou no total R${total}.
A compra mais cara feita foi do produto {bnome}, que custa {barato:.2f}.""")
if bcount == 0:
    print("Nenhum dos seus produtos comprados têm o valor maior do que R$1000.")
elif bcount == 1:
    print("Apenas um de seus produtos tem o valor maior do que R$1000.")
elif bcount > 1:
    print(f"Você comprou {bcount} produtos com valor maior do que R$1000.")
