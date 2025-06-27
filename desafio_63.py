termos = int(input("Digite o número de termos que você quer que a sequência de Fibonacci tenha: "))
a = 0
s = 1
c = 3
print("{} -> {}".format(a, s), end="")
while c <= termos:
    c += 1
    t = a + s

    a = s
    s = t
    print("-> {}".format(t), end="")
print("")
print("end")

# MUITA LÓGICA ENVOLVIDA PRO MEU CEREBELINHO RACIOCINAR EM 2H.
# Mas abre uma ideia mais aberta entre as possibilidades que eu posso fazer, como o exercício