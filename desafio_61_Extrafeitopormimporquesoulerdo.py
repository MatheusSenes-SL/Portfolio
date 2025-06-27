cond = ""
c = 0
sm = 0
while cond != "N":
    num = int(input("Digite um número para o cálculo de média aritmética: "))
    sm += num
    c += 1
    cond = str(input("Deseja adicionar mais um número [S/N]? ")).strip().upper()
media = (sm / c)
print("""O resultado desse cálculo é {}:
{} / {} = {}""".format(media, sm, c, media))