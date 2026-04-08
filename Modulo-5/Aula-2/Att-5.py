import math

def calcula_perimetro_triangulo(a, b, c):
    return a + b + c


def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio


def calcula_perimetro_retangulo(lado1, lado2=None):
    if lado2 is None:
        return 4 * lado1
    else:
        return 2 * (lado1 + lado2)


while True:
    print("\n1 - Calcular perímetro triângulo")
    print("2 - Calcular perímetro círculo")
    print("3 - Calcular perímetro retângulo")
    print("4 - Sair")

    opcao = int(input("\nOpção: "))

    if opcao == 1:
        print("Digite os três lados do triângulo:")
        a = int(input())
        b = int(input())
        c = int(input())
        print("O perímetro é:", calcula_perimetro_triangulo(a, b, c))

    elif opcao == 2:
        raio = int(input("Digite o raio do círculo: "))
        print("O perímetro é:", calcula_perimetro_circulo(raio))

    elif opcao == 3:
        print("Informe os dois lados do retângulo. Se for um quadrado, digite 0 para o segundo valor:")
        lado1 = int(input())
        lado2 = int(input())

        if lado2 == 0:
            print("O perímetro é:", calcula_perimetro_retangulo(lado1))
        else:
            print("O perímetro é:", calcula_perimetro_retangulo(lado1, lado2))

    elif opcao == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")