num1 = float(input("Digite um número real para saber sua tabuada até 20: "))
print("{}".format('-=-=-' * 6))
for a in range(1, 21):
    print("{:.2f} x {:.2f} = {:.2f}".format(num1, a, (num1 * a)))
print("{}".format('-=-=-' * 6))
