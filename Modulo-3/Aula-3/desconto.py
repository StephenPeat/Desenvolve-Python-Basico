compra = float(input("Digite o valor da compra: "))

if compra < 50:
    print("Sua compra não tem valor suficiente para desconto, total da compra R$", compra)

elif 50 <= compra < 100:
    desconto = compra - (compra * 0.10)
    print("Com desconto sua compra fica R$", desconto)

else:
    desconto = compra - (compra * 0.20)
    print("Com desconto sua compra fica R$", desconto)