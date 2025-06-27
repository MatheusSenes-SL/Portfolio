pal = str(input("Digite uma palavra para verificar se é um palíndromo: ")).strip().lower()
palavras = (pal.split())
junto = ''.join(palavras)
inverso = ''  # Você pode ao invés de usar for, apenas usar inverso = junto[::-1]
print(junto)
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Este é um palíndromo.")
else:
    print("Este não é um palíndromo.")