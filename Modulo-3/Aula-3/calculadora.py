n1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /, **): ")
n2 = float(input("Digite o segundo número: "))

if operador == "+":
    print("Resultado:", n1 + n2)

elif operador == "-":
    print("Resultado:", n1 - n2)

elif operador == "*":
    print("Resultado:", n1 * n2)

elif operador == "/":
    print("Resultado:", n1 / n2)

elif operador == "**":
    print("Resultado:", n1 ** n2)

else:
    print("Operação inválida.")