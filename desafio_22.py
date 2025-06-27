nome = str(input("Digite seu nome: ")).strip()  # Pode se colocar strip aqui.
high = (nome.upper())
low = (nome.lower())
nome2 = (nome.split())
print("O seu nome em maiúsculo é: {}".format(high))
print("Seu nome em minúsculo é: {}".format(low))
print("Seu nome tem {} letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(len(nome2[0])))

# OBSERVAÇÕES:
# Para resolver sobre a quantidade de letras no primeiro nome, dá para fazer:
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
# Mas eu acho que não é uma boa ideia se o nome tiver 1 palavra só, então prefiro o que usei.
