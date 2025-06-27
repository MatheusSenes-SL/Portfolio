num = int(input("Digite um número de 0 a 9999: "))
n = str(num)
separado = (n.split())
print("O seu número é o {} \nEle é composto por:".format(n))
print("{} unidade(s)".format(separado[0][3]))
print("{} dezena(s)".format(separado[0][2]))
print("{} centena(s)".format(separado[0][1]))
print("{} milhar(es)".format(separado[0][0]))

# 0BS:
# Não é necessário usar o [0], pode ser feito direto neste caso.
# Eu adicionei n = str(num) porque a pessoa pode escrever letras ao invés de números.
# Há como fazer usando matemática e protegendo o limite de algarismos (que é 4) fazendo o seguinte:
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("A unidade é {}, a dezena é {}, A centena é {} e o milhar é {}".format(u, d, c, m))
