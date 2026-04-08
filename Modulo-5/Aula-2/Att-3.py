def soma_digitos(n):
    soma = 0
    
    while n > 0:
        digito = n % 10      
        soma += digito      
        n = n // 10          
    
    return soma
numero = int(input("Digite um número inteiro: "))

resultado = soma_digitos(numero)

print("A soma dos dígitos é:", resultado)