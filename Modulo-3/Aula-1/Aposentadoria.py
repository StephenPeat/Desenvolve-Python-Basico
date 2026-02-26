print("Selecione seu gênero:")
print("1 - Masculino")
print("2 - Feminino")
opcao_genero = input("Escolha uma opção: ")
genero = {"1": "Masculino", "2": "Feminino"}[opcao_genero]
idade = int(input("Digite quantos anos você tem: "))
tempo_servico = int(input("Digite quantos anos você está na área: "))
aposentar = (genero == "Masculino" and idade >= 65) or (genero == "Feminino" and idade >= 60) or (tempo_servico >= 30) or ((idade >=60) and (tempo_servico >=25))
print(aposentar)
if aposentar:
    print("Você já está apto a se aposentar.")
else:
    print("Você ainda não está apto a se aposentar.")