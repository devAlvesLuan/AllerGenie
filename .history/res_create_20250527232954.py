import json
import pwinput
from validacoes import *

class Restaurante:
    
    """
    Representa um cliente do aplicativo AllerGenie.

    Atributos:
    nome_restaurante (str): Nome do restaurante 
    | cnpj (str): CNPJ da empresa/restaurante
    | email (str): Email do restaurante 
    | senha_1 (str): Senha do usuário

    """
    
    
    
    def __init__(self, nome_restaurante, cnpj, email, senha_1): #Adiciona atributos às instâncias
        self.nome_restaurante = nome_restaurante 
        self.cnpj = cnpj
        self.email = email
        self.senha = senha_1


    def criador_dic(self): #Converte todas as intâncias em dicionarios
        return {
            "nome": self.nome_restaurante,
            "cnpj": self.cnpj,
            "email": self.email,
            "senha": criptografador(self.senha), #Criptografa a senha inserida
            "id": str(id(self.email))
        }

def res_create():



    dados = []
    caminho_json = 'restaurantes.json' #Nomeia arquivo JSON
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    print("================================================================\n          ---- Seja bem-vindo a tela de cadastro! ----\n================================================================")

    cnpj_opc = False
    execucao_opc = True
    while True:
        nome_emp = input('----------------------------\n  Insira o nome da empresa: ')
        if validador_nome(nome_emp):
            break

    while execucao_opc:
            opcao = input('----------------------------\n  Incluir CNPJ? (Opcional)\n 1. Sim\n 2. Não\n')
            if opcao == '2': #Realiza a checagem de se a tecla pressionada é válida ou não e qual a opção selecionada
                cnpj_opc = False
                execucao_opc = False
                break
            elif opcao == '1':
                cnpj_opc = True
                execucao_opc = False
                break
            else:
                print('Erro: Inserção inválida')

    if cnpj_opc: #Checa se o usuário quer inserir CNPJ ou não
        while True:
            cnpj = input('----------------------------\n  Insira seu CNPJ:')
            if validador_cnpj(cnpj_opc, cnpj, dados):
                break
    else:
        cnpj = 'Não cadastrado.'

    while True:
        email_emp = input('----------------------------\n  Insira seu email (Exemplo: cleyton@gmail.com):').lower().strip()
        if validador_email(email_emp, dados):
            break

    while True:
        senha_emp = pwinput.pwinput(prompt='----------------------------\n  Insira sua senha (Ela deve incluir pelo menos 10 caractéres, uma letra maiúscula e dois número):', mask = '*')
        confirm_senha = pwinput.pwinput(prompt='----------------------------\n  Insira sua senha novamente:', mask = '*')
        if validador_senha(senha_emp, confirm_senha):
            break
    
    print('Cadastro realizado com sucesso.')
    restaurant = Restaurante(nome_emp, cnpj, email_emp, senha_emp) #Cria objeto

    dados.append(restaurant.criador_dic()) #Adiciona dados ao arquivo

    with open(caminho_json, 'w', encoding='utf-8') as f: #Salva dados alterados
        json.dump(dados, f, indent = 4, ensure_ascii= False)