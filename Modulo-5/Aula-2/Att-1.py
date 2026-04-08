def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

n = int(input("Digite um número inteiro: "))

resultado = fatorial(n)

print("O fatorial de", n, "é", resultado)