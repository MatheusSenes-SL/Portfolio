num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
cnum1 = ("\033[2;34m{}\033[m".format(num1))
cnum2 = ("\033[2;35m{}\033[m".format(num2))
if num1 > num2:
    print("O primeiro valor ({}) é o maior, enquanto o outro ({}) é o menor.".format(cnum1, cnum2))
elif num2 > num1:
    print("O segundo valor ({}) é o maior, enquanto o outro ({}) é o menor.".format(cnum2, cnum1))
else:
    print("\033[1;36mTanto o valor 1 quanto o valor 2 remetem ao número {}. \033[m".format(cnum1 or cnum2))
