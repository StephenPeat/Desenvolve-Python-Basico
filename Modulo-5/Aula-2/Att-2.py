def soma_quadrados(a, b):
    return a**2 + b**2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resultado = soma_quadrados(n1, n2)

print("A soma dos quadrados é:", resultado)