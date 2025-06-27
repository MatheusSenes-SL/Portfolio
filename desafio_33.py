a = int(input("Primeiro Valor: "))
b = int(input("Segundo Valor: "))
c = int(input("Terceiro Valor: "))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = b
print(menor)
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(maior)
