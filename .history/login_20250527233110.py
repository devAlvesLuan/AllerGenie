from menu_cliente import *
from menu_restaurante import *

def login(caminho_json):
    
    """
    Realiza a pesquisa por restaurantes com base no nome.

    Parâmetros:
    pesquisa (str): Termo de busca inserido pelo usuário.

    Retorna:
    list: Lista de tuplas contendo informações dos restaurantes encontrados.
    """
    
    
    print("================================================================\n          ---- Seja bem-vindo a tela de login! ----\n================================================================")

    caminho = caminho_json
    with open(caminho, 'r', encoding='utf-8') as file:
        banco_dados = json.load(file)

    executando = True

    while executando:

        email = str(input("----------------------------\nDigite seu email: ").strip().lower())

        usuario_encontrado = None

        for usuario in banco_dados:
            if usuario.get('email') == email:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            senha = pwinput.pwinput(prompt='----------------------------\nInsira sua senha: ', mask='*')
            if usuario_encontrado.get('senha') == criptografador(senha):
                print("-- Login realizado com sucesso! --")
                if 'cnpj' not in usuario_encontrado:
                    menu_cliente(usuario_encontrado)
                else:
                    menu_empresa(usuario_encontrado)
            else:
                print("----------------------------\nErro: Senha inválida.")
        else:
            print("----------------------------\nErro: Email não cadastrado.")