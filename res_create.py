import json
import pwinput
from validacoes import *
from crud_geral import CrudRestaurante, CRUD
from util import *

def res_create():
    """
    - Inserção de dados para a criação do objeto Restaurante
    """

    dados = []
    caminho_json = 'bancos_json/restaurantes.json' #Nomeia arquivo JSON
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    print(Utils.pinta("================================================================\n          ---- Seja bem-vindo a tela de cadastro! ----\n================================================================", 'verde_claro'))

    cnpj_opc = False
    execucao_opc = True
    while True:
        print(Utils.pinta('----------------------------', 'ciano'))
        nome_emp = input('Insira o nome da empresa: ')
        if validador_nome(nome_emp):
            break

    while execucao_opc:
            print(Utils.pinta('----------------------------', 'ciano'))
            print('Incluir CNPJ? (Opcional)\n 1. Sim\n 2. Não')
            opcao = input('> ')
            if opcao == '1':
                cnpj_opc = True
                execucao_opc = False
                break
            elif opcao == '2': #Realiza a checagem de se a tecla pressionada é válida ou não e qual a opção selecionada
                cnpj_opc = False
                execucao_opc = False
                break
            else:
                print('Erro: Inserção inválida')

    if cnpj_opc: #Checa se o usuário quer inserir CNPJ ou não
        while True:
            print(Utils.pinta('----------------------------', 'ciano'))
            cnpj = input('Insira seu CNPJ:')
            if validador_cnpj(cnpj_opc, cnpj, dados):
                break
    else:
        cnpj = 'Não cadastrado.'

    while True:
        print(Utils.pinta('----------------------------', 'ciano'))
        email_emp = input('Insira seu email (Exemplo: cleyton@gmail.com):').lower().strip()
        if validador_email(email_emp, dados):
            break

    while True:
        print(Utils.pinta('----------------------------', 'ciano'))
        senha_emp = pwinput.pwinput(prompt='Insira sua senha (Ela deve incluir pelo menos 10 caractéres, uma letra maiúscula e dois número):', mask = '*')
        confirm_senha = pwinput.pwinput(prompt='Insira sua senha novamente:', mask = '*')
        if validador_senha(senha_emp, confirm_senha):
            break
    
    Utils.limpar_tela()
    print(Utils.pinta('-- Cadastro realizado com sucesso! --', 'magenta_claro'))
    restaurant = CrudRestaurante(nome_emp, email_emp, senha_emp, cnpj) #Cria objeto

    dados.append(restaurant.criador_dic()) #Adiciona dados ao arquivo

    CRUD.salvar_dados(caminho_json, dados)