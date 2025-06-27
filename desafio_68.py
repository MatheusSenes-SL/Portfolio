#-~=-~=-~=-~=-~=-~=-~=-~=-~=-~=-~=JOGO PAR OU ÍMPAR-~=-~=-~=-~=-~=-~=-~=-~=-~=-~=-~=-
#--------------------------------------Variáveis-------------------------------------
import random
from time import sleep
cont = win = escolha = lose = player = par = soma = NPC = 0
vt = ["Ah, você ganhou!", "Eu te venço na próxima!", "Você vai perder!", "Para de ganhar!"]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=INÍCIO DO PROGRAMA=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
while True:
    NPC = random.randint(0, 50)
    escolha = str(input("Você prefere ímpar ou par[I/P]? ")).strip().upper()
    #print(NPC)  #<-- Para testes
    player = int(input("Digite um número: "))
    if escolha[0] == "P":
        par = "par"
    elif escolha[0] == "I":
        par = "impar"
    else:
        print("É algum tipo de brincadeira nova do Ímpar ou Par? Eu não quero jogar então!")
        break
    soma = NPC + player
    print("Ímpar, ", end="")
    sleep(0.5)
    print("par!")
    print("1, 2, 3. Vamos e...", end="")
    sleep(0.5)
    print(" já!")
    sleep(0.5)
    print("Umm.. ", end="")
    sleep(0.5)
    print(f"Você escolheu {par} e lançou {player}. Isso somado com minha escolha, {NPC}, dá {soma}.")
    sleep(0.5)
    if escolha[0] == "P" and soma % 2 == 0 or escolha[0] == "I" and soma % 2 != 0:
        print(random.choice(vt))
        cont += 1
    elif escolha[0] == "P" and soma % 2 != 0 or escolha[0] == "I" and soma % 2 == 0:
        break

if par == "par" or par == "impar":
    if cont == 0:
        print("Hah! Você não ganhou de mim nenhuma vez... dessa vez... Tudo bem, boa sorte na próxima!.")
    elif cont == 1:
        print("Eu não ia deixar barato aquela vitória, haha!")
    else:
        print(f"Você perdeu após a {cont}° vitória, Puxa!. Parabéns por me vencer até a {cont}° vez!")
