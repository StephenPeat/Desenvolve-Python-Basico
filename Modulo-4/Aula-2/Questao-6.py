numero = int(input("Digite um número (0 para parar): "))

if numero == 0:
    print("Nenhum número foi digitado.")
else:
    maior = numero
    menor = numero

    while True:
        numero = int(input("Digite um número (0 para parar): "))
        
        if numero == 0:
            break
        
        if numero > maior:
            maior = numero
        
        if numero < menor:
            menor = numero

    print("Maior:", maior)
    print("Menor:", menor)