nome = str(input("Digite seu nome: ")).title().strip().split()
print("Bem-vindo ao nosso programa, {}!".format(' '.join(nome)))
print("""Nome completo: {}
Primeiro nome: {}
último nome: {} """.format(' '.join(nome), nome[0], nome[len(nome)-1]))
