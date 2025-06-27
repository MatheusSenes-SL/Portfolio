# Faça um programa que leia algo e mostre na tela o seu tipo primitivo e todas as informações sobre ele.
num1 = (input("digite um número legal (= :"))
tipo = (type(num1))
print("Qual é o tipo primitivo?".format(tipo))
numeric = (num1.isnumeric())
print("É apenas numérico?".format(numeric))
alfabeto = (num1.isalpha())
print("É apenas alfabético?".format(alfabeto))
ambos = (num1.isalnum())
print("Tem números e letras? {}".format(ambos))
# entre outros "In_alguma_coisa()"
# OBSERVAÇÃO IMPORTANTE: PARA VERIFICAR, TEM QUE TER () NO FINAL, como nos exemplos acima.
# TAMBÉM É BOM USAR O ".FORMAT" PARA TREINAR.