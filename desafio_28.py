import random
import time
num = [1, 2, 3, 4, 5]
got = random.choice(num)
ask = int(input('Eu escolhi um número de 1 a 5. Qual acha que escolhi?'))
print("Uhmm... Rufem os tambores!!!")
time.sleep(2)
if ask == got:
    print("\033[2;32mVocê acertou, eu escolhi o número {}. Parabéns!\033[m".format(got))
else:
    print("\033[2;31mNão, você errou, eu escolhi o número {}. Eu ganhei!\033[m".format(got))
print('end')

# Para deixar mais dinâmico, pode usar o pacote 'time', que adiciona tempo.
# O time.sleep pode fazer ele demorar um pouco antes de responder, dando um pouco de tensão!