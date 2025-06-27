termos = int(input("Digite o número de termos que você quer que a sequência de Fibonacci tenha: "))
a = 0
s = 0
t = 0
while a != termos:
    a += 2
    s += a - 1
    t = s
    print("{:.0f}".format(t), end="")
    print("{}".format(" -> "), end="")
print("end")
