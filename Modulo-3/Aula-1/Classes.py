classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

valido = (
    (classe == "guerreiro" and forca >= 15 and magia <= 10) or
    (classe == "mago" and forca <= 10 and magia >= 15) or
    (classe == "arqueiro" and forca > 5 and magia > 5 and forca <= 15 and magia <= 15)
)

if valido:
    print("True")
    print("Os pontos de atributos são compatíveis com a classe escolhida.")
else:
    print("False")
    print("Os pontos de atributos não são compatíveis com a classe escolhida.")