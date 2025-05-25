import json
from res_create import *

def executar_login():
    print("---- Seja bem-vindo a tela de login! ----")
    login()

caminho = 'restaurantes.json'

def login():

    def autentificador(operacao, insercao):
        for usuario in restaurantes:
            if usuario.get(operacao) == insercao:
                 return True
            else:
                 return False
    
    with open(caminho, 'r', encoding='utf-8') as file:
        restaurantes = json.load(file)
    
    email = str(input("Seu email: "))
    email = email.strip()

    if autentificador('email',email):
        print('Deu certo o email')
    else:
        print('Deu ruim o email')

    senha = str(input("Digite sua senha: "))
    senha = senha.strip()

    if autentificador('senha',senha):
        print('Deu certo a senha')
    else:
        print('Deu ruim a senha')

        
    # for usuario in lista_usuario:
    #     if usuario.get(nome) == nome_usuario:


    # if (email == "luanmarcos03@hotmail.com" and senha == "123"):
    #     print("-- Login realizado com sucesso!!! --")
    #     # vai pro menu
    # else: 
    #     print("Erro: Dados incorretos, digite novamente.")