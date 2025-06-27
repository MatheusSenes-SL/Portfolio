num = int(input("Digite um número qualquer para receber sua forma em \033[1;32mbinário, \033[1;31moctal,\033[1;34m decimal\033[m: "))
forma = str(input("Digite a formas que quer escolher: ")).strip().title().split()
if "Binário" in forma or "Binario" in forma:
    print("\033[0;32mBinário\033[m: ", ((bin(num)).replace("0b", "")))
elif "Octal" in forma:
    print("\033[0;31mOctal\033[m:", ((oct(num)).replace("0o", "")))
elif "Decimal" in forma:
    print("\033[0;34mDecimal\033[m: ", ((hex(num)).replace("0x", "")))
else:
    print("Você tem certeza que escreveu corretamente essas formas?\nNão foi possível verificar o código.")

# OBS: Você pode usar os comandos abaixo para conferir, apenas retire a "#" (hashtag):
#print("{}\nOlhe embaixo para conferir".format("=" * 40))
#print("binario", bin(num))
#print("octal", oct(num))
#print("decimal", hex(num))

# Eu poderia ter usado um sistema mais simples de números, mas ainda acho que o meu está um pouco bom.
# Mesmo que esteja bem bagunçado... Desculpe mandamentos do Python.