paridade = lambda x: "par" if x % 2 == 0 else "ímpar"

print("Digite os valores que deseja verificar a paridade (digite 0 para finalizar a entrada de dados):")

while True:
    numero = int(input())

    if numero == 0:
        break
