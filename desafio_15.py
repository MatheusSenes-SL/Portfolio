diario = int(input("Por quantos dias o carro foi alugado? "))
rodado = float(input("Quantos quilômetros foram rodados? "))
v_diario = 60
v_rodado = 0.15
result = ((diario * 60) + (rodado * v_rodado))
print("Você deve pagar no total {:.2f}.".format(result))
