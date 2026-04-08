import random
import math

n = int(input("Digite o valor de n: "))

soma = 0

for i in range(n):
    numero = random.randint(0, 100)
    soma = soma + numero

resultado = math.sqrt(soma)

print("A raiz quadrada da soma é:", resultado)