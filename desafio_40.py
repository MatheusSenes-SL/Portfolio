nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = ((nota2 + nota1) / 2)
maxi = 25
if media >= maxi:
    print("\033[1;31mTem algo errado. A nota máxima é 25!\033[m")
elif media >= 7:
    print("\033[1;35mParabéns! Você foi aprovado!\033[m")
elif 5.0 < media < 6.9:
    print("\033[1;33mNão se preocupe, mas você precisa se esforçar mais. Está de recuperação. \033[m")
elif media < 5.0:
    print("\033[1;32mBem... Você não pode ser aprovado. Mas não desista de estudar... Assim você vai conseguir passar!.")
print("end")
