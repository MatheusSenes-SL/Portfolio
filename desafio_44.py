val = int(input("Qual o valor do produto? "))
pag = str(input("Qual o tipo de pagamento? ")).strip().lower()
ten = ((val * 10) / 100)
fiv = ((val * 5) / 100)
twenty = ((val * 20) / 100)
if ("dinheiro" and "vista" in pag) or ("cheque" and "vista" in pag):
    # ERRO BOBÍSSIMO! SEMPRE QUANDO FOR USAR 'OR', COLOQUE O VARIÁVEL NA SEQUÊNCIA DE ANTES E DEPOIS, SENÃO ELE VAI CRASHAR O CÓDIGO TODO.
    # EX: ("dinheiro" and "vista") or ("cheque" and "vista") in pag): NÃO VAI FUNCIONAR PORQUE NÃO ESTÃO DIRECIONADOS AOS SEUS PRÓPRIOS VALORES DE pag.
    # ("dinheiro" and "vista" in pag) or ("cheque" and "vista" in pag): É O CORRETO, POIS ADICIONOU UM pag PARA CADA VALOR ("dinheiro" por exemplo).
    print("Os métodos de pagamento à vista de dinheiro ou cheque recebem 10% de desconto, logo o produto ficará R${}".format(val - ten))
elif "cartão" and "vista" in pag:
    print("Os método de pagamento à vista por cartão recebe 5% de desconto, logo o produto ficará R${}.".format(val - fiv))
elif "cartão" and "2x" in pag:
    print("A partir do pagamento parcelado em 2 vezes, o valor não será descontado, logo ainda custará {}".format(val))
elif "cartão" and "3x" in pag:
    print("A partir do pagamento parcelado em 3 vezes, o valor recebe um juros de 20%, logo o produto ficará R${}".format(val + twenty))
else:
    print("Não foi possível realizar a compra do produto. Tente novamente.")

# Eu não usei o sistema numérico do professor, logo o dele é mais tranquilo e menos complexo do que o meu.