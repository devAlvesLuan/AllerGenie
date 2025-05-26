<<<<<<< HEAD
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
=======
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
                break

        if usuario_encontrado:
            senha = pwinput.pwinput(prompt='----------------------------\nInsira sua senha:', mask = '*')
            if usuario.get('senha') == criptografador(senha):
                print("-- Login realizado com sucesso! --")
                executando = False
            else:
                print("----------------------------\nErro: Senha inválida.")
        else:
            print("----------------------------\nErro: Email não cadastrado.")
>>>>>>> 3c285407bfe2d943bd16bf0a89f9e09d63e6bf15
