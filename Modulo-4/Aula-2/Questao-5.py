N = int(input("Quantas linhas (N)? "))
M = int(input("Quantas colunas (M)? "))

print(" ", end=" ")
for coluna in range(1, M + 1):
    print(coluna, end=" ")
print()

for linha in range(1, N + 1):
    print(linha, end=" ")
    for coluna in range(M):
        print("/", end=" ")
    print()