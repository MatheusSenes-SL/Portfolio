sexo = ""
while sexo != "M" and sexo != "F":  #Eu poderia ter usado 'while sexo not in "MmFf":', mas eu já aprendi a usar 'and'.
    sexo = str(input("Por favor, informe seu sexo[M para masculino/F para feminino]: ")).strip().upper()[0]  #<--- Isso é bastante útil para pegar apenas a primeira letra.
    if sexo != "M" and sexo != "F":
        print("Tente novamente.")
print("O seu sexo foi validado com sucesso! Agradecemos pela compreensão!")