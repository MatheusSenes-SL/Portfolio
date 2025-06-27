altura = float(input("Qual a sua altura em metros? "))
peso = float(input("Qual o seu peso em quilos? "))
imc = (peso / altura ** 2)
print("O seu IMC é de {.:2f}.".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso ideal. Cuidado, isso pode prejudicar sua saúde.")
elif 18.5 < imc < 25:
    print("Você está no peso ideal. Isso é bom para você, continue cuidando da sua saúde!")
elif 25 < imc < 30:
    print("Você está no estágio de sobrepeso. Não é um problema, mas tome cuidado para não virar um.")
elif 30 < imc < 40:
    print("Você está no estágio de obesidade. É preciso que você faça uma visita a um médico para analisar a gravidade do seu caso.")
elif imc > 40:
    print("Você é um paciente com obesidade mórbida. O seu caso é bastante grave, portanto é preciso que faça todo um procedimento para melhorar sua saúde")
print("end")
