# h² = a² * b² // Calcule a hipotenusa
import math
co = math.pow(float(input("Digite o cateto oposto: ")), 2)
ca = math.pow(float(input("Digite o cateto adjacente: ")), 2)
print('A soma da raiz de {} com  a raiz de {} é igual a hipotenusa'.format(co, ca))
print('O valor da hipotenusa é {}'.format(math.sqrt(co + ca)))

# A biblioteca 'math' tem o comando "hypot" para calcular a hipotenusa. Assim pode-se fazer:
Co = float(input("Comprimento do Cateto Oposto: "))
Ca = float(input("Comprimento do Cateto Adjacente: "))
hypo = math.hypot(Co, Ca)
print("Com o cateto oposto sendo {}cm² e o cateto adjacente sendo {}cm², a hipotenusa mede {} cm²".format(Co, Ca, hypo))

# Ou você pode fazer sem o uso de uma biblioteca apenas com:
hipotenusa = ((co ** 2) + (ca ** 2) ** (1/2))
print(hipotenusa)
