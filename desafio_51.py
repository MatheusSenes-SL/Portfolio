nome = str(input("Qual o seu nome? ")).strip().title()
print("Olá, {}. Preciso que você digite as informações a seguir:".format(nome))
a1 = int(input("Primeiro termo da PA: "))
n = int(input("Posição do termo que queremos descobrir: "))
r = int(input("Razão: "))
t_geral = a1 + (n - 1) * r
# print(t_geral)
print("Sendo o valor do primeiro número da P.A. {}, podemos descobrir na {}° posição o número {} através da razão {}".format(a1, n, t_geral, r))
print("Assim, a P.A. vai ser a seguinte:")
for c in range(a1, t_geral + 1, r):
    print(' {}'.format(c), end=' , ')

print('end')