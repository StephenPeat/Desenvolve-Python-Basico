def inverteValor(n):
    invertido = 0
    
    while n > 0:
        digito = n % 10
        invertido = invertido * 10 + digito
        n = n // 10
    
    return invertido


def verificaInverso(original, invertido):
    if (original % 2 == invertido % 2):
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))

valor_invertido = inverteValor(numero)

print("Valor invertido:", valor_invertido)
print("Possuem a mesma paridade?", verificaInverso(numero, valor_invertido))