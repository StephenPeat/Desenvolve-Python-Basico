Pontos = int(input("Quantos jogos o cruzeiro fez:"))

vitorias = 0
empates = 0
derrotas = 0

for i in range(Pontos):
    gols_cruzeiro = int(input("Quantos gols o cruzeiro fez:"))
    gols_oponente = int(input("Quantos gols o adversario fez:"))
    
    if gols_cruzeiro > gols_oponente:
        vitorias = vitorias + 1
    elif gols_cruzeiro == gols_oponente:
        empates = empates + 1
    else:
        derrotas = derrotas + 1

pontuacao = (vitorias * 3) + (empates * 1)

print ( )
print("Vitórias:", vitorias)
print("Empates:", empates)
print("Derrotas:", derrotas)
print("Pontuação:", pontuacao)
print ( )