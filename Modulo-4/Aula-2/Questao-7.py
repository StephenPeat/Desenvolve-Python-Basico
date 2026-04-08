produto = 1      
saida = 1        

while True:
    numero = int(input("Digite um número inteiro (0 para parar):"))
    
    if numero == 0:
        break
    
    if numero > 0:
        produto = produto * numero
    
    if numero < 0:
        saida = saida * numero

print()
print("Produto dos positivos:", produto)
print("Produto dos negativos:", saida)
print()