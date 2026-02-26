idade = int(input("Digite sua idade: "))
jogos_jogados = int(input("Quantos jogos de tabuleiro você já jogou? "))
vitorias = int(input("Quantos jogos você já venceu? "))

apto = (idade >= 16 and idade <= 18) and jogos_jogados >= 3 and vitorias >= 1

print("Apto para ingressar no clube de jogos de tabuleiro:", apto)
if jogos_jogados > 0:
    porcentagem = (vitorias / jogos_jogados) * 100
    print("Porcentagem de vitórias:", porcentagem, "%")