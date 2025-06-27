import datetime
import time
nome = str(input("Qual o seu nome? ")).strip().title()
anoq = int(input("Que ano nasceu? "))
data = datetime.date.today().year
vai = str(input("Pretende se alistar para o exército? ")).strip().lower()
idade = (data - anoq)
falta = (18 - idade)
time.sleep(1)
print("Tudo bem... Aguarde uns segundos...")
time.sleep(2)
if idade < 18:
    print("Você vai se alistar? Faltam {} anos para se alistar.".format(falta))
elif idade == 18:
    if "sim" in vai:
        print("Você já pode se alistar este ano.")
    else:
        print("Agora que vai ser pego mesmo.")
else:
    if "não" in vai or "nao" in vai:  # TEM QUE ADICIONAR A VARIÁVEL ANTES E DEPOIS DO OR!!
        print("Tudo bem. Portanto você não tem mais idade para se alistar.")
    else:
        print("Entendi. Mas você já passou da idade de se alistar.")
