usuarios = {
    "admin": {"senha": "admin123", "nivel": "Administrador"},
    "usuario1": {"senha": "senha123", "nivel": "Usuário Comum"},
    "visitante1": {"senha": "guest2024", "nivel": "Visitante"}
}

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario in usuarios:
    if senha == usuarios[usuario]["senha"]:
        print("Login realizado com sucesso!")
        print("Nível de acesso:", usuarios[usuario]["nivel"])
    else:
        print("Erro: Usuário ou senha inválidos.")
else:
    print("Erro: Usuário ou senha inválidos.")