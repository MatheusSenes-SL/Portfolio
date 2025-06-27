s = 0
confirm = str(input('Digite "ok" se confirma a operação: ')).strip().lower()
if confirm == 'ok':
    for a in range(0, 6,):
        num = int(input("num: "))
        if num % 2 == 0 and num % 2 != 1:
            s += num
            print("Até agora o resultado é {}.".format(s))

print("end")