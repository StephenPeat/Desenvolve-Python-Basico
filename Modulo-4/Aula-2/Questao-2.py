numero = int(input("Digite um número: "))

soma = 0

for sequencia in range(1, numero + 1):
    soma = soma + sequencia

print(f"A soma dos números de 1 a {numero} é {soma}")