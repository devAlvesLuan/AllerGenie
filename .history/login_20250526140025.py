from res_create import *

def login(caminho_json):
    print("================================================================\n          ---- Seja bem-vindo a tela de login! ----\n================================================================")

    caminho = caminho_json
    with open(caminho, 'r', encoding='utf-8') as file:
        banco_dados = json.load(file)

    executando = True

    while executando:

        email = str(input("----------------------------\nSeu email: ").strip())

        usuario_encontrado = None

        for usuario in banco_dados:
            if usuario.get('email') == email:
                usuario_encontrado = usuario
                id_usuario = usuario.get(id)
                break

        if usuario_encontrado:
            senha = input('----------------------------\nInsira sua senha:', mask = '*')
            if usuario.get('senha') == criptografador(senha):
                print("-- Login realizado com sucesso! --")
                executando = False
            else:
                print("----------------------------\nErro: Senha inválida.")
        else:
            print("----------------------------\nErro: Email não cadastrado.")