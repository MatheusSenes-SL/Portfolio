import datetime
ano = int(input("Digite um ano qualquer: "))
bis = (ano % 4 and ano % 100 or ano % 400)
if ano == 0:
    ano = datetime.date.today().year
if bis == 0:
    print("Esse é um ano bissexto")
else:
    print("Esse é um ano comum")
print("end")

# O pacote datetime possui ferramentas para calcular tempo, como pode ser visto.
