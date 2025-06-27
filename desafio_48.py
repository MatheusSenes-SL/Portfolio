soma = 0
cont = 0  # O nome dessa técnica é acumulante e serve para gastar menos memória do processador
for a in range(1, 501, 2):
    if a % 3 == 0:
        cont = cont + 1
        soma += a
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma), end=' ')
