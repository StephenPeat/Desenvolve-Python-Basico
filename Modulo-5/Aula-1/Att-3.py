import random

escolhido = random.randint(1, 10)

while True:
    numero = int(input("Digite um número: "))

    if numero == escolhido:
        print("Você acertou!!")
        break
    elif numero > escolhido:
        print("Muito alto, tente novamente")
    else:
        print("Muito baixo, tente novamente")

