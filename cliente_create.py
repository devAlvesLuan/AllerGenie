import json
import pwinput
from validacoes import *
from crud_geral import CRUD
from util import *

def cliente_create():
    
    """
    - Inserção de dados para a criação do objeto
    """

    dados = []

    caminho_json = 'bancos_json/clientes.json' #Nomeia arquivo JSON
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    print(Utils.pinta("================================================================\n          ---- Seja bem-vindo a tela de cadastro! ----\n================================================================", 'verde_claro'))
    while True:
        print(Utils.pinta('----------------------------', 'ciano'))
        nome_cliente = input('Insira seu nome: ')
        if validador_nome(nome_cliente):
            break
    while True:
        print(Utils.pinta('----------------------------', 'ciano'))
        email_cliente = input('Insira seu email (Exemplo: cleyton@gmail.com):').lower().strip()
        if validador_email(email_cliente, dados):
            break

    while True:
        print(Utils.pinta('----------------------------', 'ciano'))
        senha_cliente = pwinput.pwinput(prompt='Insira sua senha (Ela deve incluir pelo menos 10 caractéres, uma letra maiúscula e dois número):', mask = '*')
        
        confirm_senha = pwinput.pwinput(prompt='Insira sua senha novamente:', mask = '*')
        if validador_senha(senha_cliente, confirm_senha):
            break
    validado = True
    
    if validado: #Checa se todos os valores insiredos são válidos
        Utils.limpar_tela()
        print(Utils.pinta('-- Cadastro realizado com sucesso! --', 'magenta_claro'))
        
        crud_objeto = CRUD(nome_cliente, email_cliente, senha_cliente)
        clientes_json = crud_objeto.criador_dic()

        dados.append(clientes_json) #Adiciona dados ao arquivo

        CRUD.salvar_dados(caminho_json, dados)