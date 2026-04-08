opcao = int(input("Opção: "))

if opcao == 1:
    operacao = lambda a, b: a if a > b else b
else:
    operacao = lambda a, b: a if a < b else b

print("\nDigite os valores de entrada. Digite 0 para finalizar a entrada de valores.")

primeiro = True

while True:
    n = int(input())

    if n == 0:
        break

    if primeiro:
        resultado = n
        primeiro = False
    else:
        resultado = operacao(resultado, n)

if opcao == 1:
    print("\nO maior valor é:", resultado)
else:
    print("\nO menor valor é:", resultado)