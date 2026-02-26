n1 = int(input("Digite o primeiro lado: "))
n2 = int(input("Digite o segundo lado: "))
n3 = int(input("Digite o terceiro lado: "))

if n1 == n2 == n3:
    print("Triângulo Equilátero")
elif n1 == n2 or n2 == n3 or n3 == n1:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")