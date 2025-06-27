a = 0
s = 0
c = 0
while a != 999:
    a = int(input("Digite um número[999] para parar: "))
    if a != 999:  # <--- O '999' pode ser chamado de 'flag'.
        c += 1
        s += a
        #print(s, c)
    else:
        print("Programa terminado.")
print("Somando os números {} anteriores temos o valor total {}.".format(c, s))
