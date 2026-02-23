valor = int(input("Digite o valor: "))

nota100 = valor // 100
valor = valor - (nota100 * 100)

nota50 = valor // 50
valor = valor - (nota50 * 50)

nota20 = valor // 20
valor = valor - (nota20 * 20)

nota10 = valor // 10
valor = valor - (nota10 * 10)

nota5 = valor // 5
valor = valor - (nota5 * 5)

nota2 = valor // 2
valor = valor - (nota2 * 2)

nota1 = valor

print(nota100, "nota(s) de R$100,00")
print(nota50, "nota(s) de R$50,00")
print(nota20, "nota(s) de R$20,00")
print(nota10, "nota(s) de R$10,00")
print(nota5, "nota(s) de R$5,00")
print(nota2, "nota(s) de R$2,00")
print(nota1, "nota(s) de R$1,00")
