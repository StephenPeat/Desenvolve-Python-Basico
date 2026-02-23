comprimento = int(input("Digite o comprimento do terreno (m): "))
largura = int(input("Digite a largura do terreno (m): "))
area_m2 = comprimento * largura
preco_total = float(input("Digite o valor total do terreno: "))
preco_m2 = preco_total / area_m2
print(f"O terreno possui {area_m2}m2.")
print(f"O preço por metro quadrado é R${preco_m2:,.2f}")
print(f"O terreno custa R${preco_total:,.2f}")
