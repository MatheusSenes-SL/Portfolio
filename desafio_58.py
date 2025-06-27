import random
sn = ""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
got = random.choice(a)
print(got)
player = 0
if player != got:
    while player != got:
        player = int(input("Qual número você acha que é? "))
        if player < got:
            print("Uhh.. Parece que você tá abaixo dele...")
        elif player > got:
            print("Tá.. Você está acima dele agora...")
        if player != got:
            sn = str(input("Não, não é este número! Vai tentar denovo[S/N]? "))
            if sn == "N":
                print("Ah.. que pena. O número que eu pensei foi {} :P".format(got))
        else:
            print(('Parabéns! Eu escolhi o número {}!'.format(got)))
else:
    print(("Parabéns! Eu escolhi o número {}!".format(got)))

# OBS:
# O comando randint (do pacote 'random') precisa de um número inicial (a) e um número final (b).
# Desse jeito, o comando será 'random.randint(a, b)'.
# Eu não sabia usar este código, então o meu programa foi maior do que o comum, mas eficaz! (Porém ainda maior...)
