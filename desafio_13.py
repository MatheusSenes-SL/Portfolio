value = float(input("Qual o salário antigo do funcionário? R$"))
n_valor = (value + (value * 15/100))
print("Então o valor aumentou de R${:.2f} para R${:.2f}".format(value, n_valor))

# Pagamento à prazo e à vista de um carro Celta 0km 2014 preços variam entre 30 mil à 32 mil.
valor_comum = float(input("Qual o valor do Celta? R$"))
valor_taxado = (valor_comum + (valor_comum * 12/100))
print("Caso pague à vista, sairá no valor de R${:.2f}.".format(valor_comum))
print("Se optar pelo pagamento à prazo, sairá por R${}".format(valor_taxado))
