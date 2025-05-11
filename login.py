def executar_login():
    print("---- Seja bem-vindo a tela de login! ----")
    login()

def login():
    email = str(input("Seu email: "))
    senha = input("Digite sua senha: ")

    if (email == "luanmarcos03@hotmail.com" and senha == "123"):
        print("-- Login realizado com sucesso!!! --")
        # vai pro menu
    else: 
        print("Erro: Dados incorretos, digite novamente.")