import json
import pwinput
from validacoes import criptografador
from util import *


def login(caminho_json):
    
    """
    - Realiza o login do usuário, seja cliente ou empresa/restaurante.

    Parâmetros:
    caminho_json (json): Qual caminho JSON o usuário vai acessar.


    """
    
    
    print("================================================================\n          ---- Seja bem-vindo a tela de login! ----\n================================================================")

    caminho = caminho_json
    with open(caminho, 'r', encoding='utf-8') as file:
        banco_dados = json.load(file)

    executando = True

    while executando:

        print(Utils.pinta('----------------------------', 'ciano'))
        email = str(input(("Digite seu email: ")).strip().lower())

        usuario_encontrado = None

        for usuario in banco_dados:
            if usuario.get('email') == email:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            print(Utils.pinta('----------------------------', 'ciano'))
            senha = pwinput.pwinput(prompt='Insira sua senha: ', mask='*')
            if usuario_encontrado.get('senha') == criptografador(senha):
                Utils.limpar_tela()
                print(Utils.pinta("--- Login realizado com sucesso! ---", 'verde_claro'))
                return usuario_encontrado
            else:
                print(Utils.pinta('----------------------------\n', 'negrito'))
                print("Erro: Senha inválida.")
        else:
            print(Utils.pinta('----------------------------\n', 'negrito'))
            print("Erro: Email não cadastrado.")