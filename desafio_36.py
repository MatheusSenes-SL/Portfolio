nome = str(input("Digite o seu nome: ")).strip().title()  # Desnecessário para o desafio.
salario = float(input("Qual seu salário mensal? "))
casa = float(input("Valor da Casa? "))
anos = int(input("Em quanto tempo em anos pretende quitá-la? cálculo de meses automático)"))
prestacao = (casa / (anos * 12))
min = salario * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos))
print("A prestação será de R${:.2f}".format(prestacao))
if prestacao >= min:
    print('Empréstimo pode ser feito')
else:
    print("Empréstimo negado")

# Eu fiz esse exercício antes, mas estava muito bagunçado. Assim preferi refazer de acordo com professor
