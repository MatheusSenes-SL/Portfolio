C1 = float(input("Comprimento de linha 1: "))
C2 = float(input("Comprimento de linha 2: "))
C3 = float(input("Comprimento de linha 3: "))
# Cada segmento tem que ser menor que a soma do comprimento dos outros 2
if C1 < C2 + C3 and C2 < C3 + C1 and C3 < C1 + C2:
    print("Este triângulo pode ser feito.")
else:
    print("Este triângulo não pode ser feito")
print("end")

# OBS:
# Este exercício me deixou desnorteado porque eu não pensei e nem pesquisei.
# Preciso começar a fazer isso mais.