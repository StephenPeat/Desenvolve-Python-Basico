entrada = input("Digite um número ou ('fim' para sair): ")

if entrada == "fim":
    exit()
else: 
    n1 = int(entrada)
    resultado = n1
while True:
    operador = input("Digite um operador (+ ou -) ou ('fim' para sair): ")
    
    if operador == "fim":
        break
    
    n2 = input("Digite mais um número ('fim' para sair): ")
    if n2 == "fim":
        break
    n2 = int(n2)

    if operador == "+":
        resultado += n2
    elif operador == "-":
        resultado -= n2
    else:
        print( )
        print("Operador inválido! Use + ou -")
        print( )

final = resultado
print ( )
print (f"seu resultado é: {final}")
print ( )