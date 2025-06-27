c1 = float(input("Digite qual a medida do primeiro comprimento: "))
c2 = float(input("Digite qual a medida do segundo comprimento: "))
c3 = float(input("Digite qual a medida do terceiro comprimento: "))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print("Esse triângulo pode ser feito!")
    if (c1 == c2 and not c1 == c2 == c3) or (c2 == c3 and not c1 == c2 == c3) or (c1 == c3 and not c1 == c3 == c2):
        print("Esse é um triângulo Isosceles, no qual possui 2 lados com a mesma medida.")  # erro (corrigido completando o código após o 'or' em cada and not)
    elif c2 == c1 == c3:
        print("Esse é um triângulo Equilátero, no qual possui seus 3 lados iguais.")
    else:
        print("Esse é um triângulo Escaleno, no qual seus 3 lados são diferentes.")
else:
    print("Não pode ser feito um triângulo com essas medidas.")
print("end")

# Você pode usar '!=' para descrever diferença, o contrário de '==', o que é igualdade.
# Eu não vi a aula do desafio antes de fazer este e os próximos 3 desafios, então todos estão corretos, porém em uma lógica mais desorganizada.
