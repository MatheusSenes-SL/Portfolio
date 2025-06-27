import random
import time
NPC = ["pedra", "papel", "tesoura"]
escolha = random.choice(NPC)
#print(escolha)
player = str(input("Pedra, papel ou tesoura? ")).strip().lower()
print("Beleza. Está pronto? Eu estou!")
time.sleep(2)
print("PEEDRA")
time.sleep(1)
print("PAPEL")
time.sleep(1)
print("TESOOOOURA!")
time.sleep(2)
if player == escolha:
    print("Aff.. empatou, eu escolhi {}".format(escolha))
elif ("pedra" in player and escolha == NPC[2]) or ("papel" in player and escolha == NPC[0]) or ("tesoura" in player and escolha == NPC[1]):
    print("\033[1;33m Ah... Parabéns! Parece que você me venceu. eu escolhi {}... \033[m".format(escolha))
elif ("pedra" in player and escolha == NPC[1]) or ("papel" in player and escolha == NPC[2]) or ("tesoura" in player and escolha == NPC[0]):
    print("\033[1;35mHahaha! Eu ganhei com {}! TOMA ESSA! \033[m".format(escolha))
else:
    print('\033[2;31mPÓ PARAR DE ROUBAR! NÃO EXISTE ESSE TAL DE "{}" NÃO!'.format(player.upper()))
print("end")
