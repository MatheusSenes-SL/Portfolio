value = float(input("Qual o valor original do produto? R$"))
discount = ((value * 5) / 100)
New_value = (value - discount)
print("Agora este produto custa 5% (R${}) a menos, o que é equivalente à R${}".format(discount, New_value))
