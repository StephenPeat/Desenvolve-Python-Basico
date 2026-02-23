def mostrar_tabuleiro(tab):
    print("\n")
    print(" ", tab[0], "|", tab[1], "|", tab[2])
    print("-----------")
    print(" ", tab[3], "|", tab[4], "|", tab[5])
    print("-----------")
    print(" ", tab[6], "|", tab[7], "|", tab[8])
    print("\n")

def verificar_vitoria(tab, jogador):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for c in combinacoes:
        if tab[c[0]] == tab[c[1]] == tab[c[2]] == jogador:
            return True
    return False


tabuleiro = ["1","2","3","4","5","6","7","8","9"]
jogador_atual = "X"
jogadas = 0

print("❌⭕ JOGO DA VELHA - 2 JOGADORES")
mostrar_tabuleiro(tabuleiro)

while True:
    try:
        posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
        
        if posicao < 0 or posicao > 8:
            print("Número inválido! Escolha de 1 a 9.")
            continue
        
        if tabuleiro[posicao] in ["X", "O"]:
            print("Posição já ocupada! Tente novamente.")
            continue

        tabuleiro[posicao] = jogador_atual
        jogadas += 1
        
        mostrar_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"🎉 Jogador {jogador_atual} venceu!")
            break

        if jogadas == 9:
            print("🤝 Deu empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

    except ValueError:
        print("Digite apenas números de 1 a 9.")
