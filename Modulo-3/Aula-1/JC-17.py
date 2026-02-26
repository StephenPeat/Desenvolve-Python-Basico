idade_juliana = input("Digite a idade da Juliana: ")
idade_cris = input("Digite a idade da Cris: ")
pode_entrar = idade_juliana >= "18" and idade_cris >= "18"
print(pode_entrar)
if pode_entrar:
    print("Ambos são maiores de idade e podem entrar no bar.")
else:
    print("Pelo menos um deles não é maior de idade, portanto não podem entrar no bar.")