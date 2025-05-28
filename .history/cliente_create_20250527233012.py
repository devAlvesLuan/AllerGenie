import json
import pwinput
from validacoes import *

class Clientes:
    
    """
    Representa um cliente do aplicativo AllerGenie.

    Atributos:
    nome (str): Nome do cliente
    | email (str): Email do cliente
    | senha (str): Senha do cliente
    
    """
    
    
    def __init__(self, nome_cliente, email, senha_1): #Adiciona atributos às instâncias
        self.nome_cliente = nome_cliente
        self.email = email
        self.senha = senha_1

    def criador_dic(self): #Converte todas as intâncias em dicionarios
        return {
            "nome": self.nome_cliente,
            "email": self.email,
            "senha": criptografador(self.senha), #Criptografa a senha inserida
            "id": str(id(self.email))
        }


def cliente_create():
    
    """
    - Inserção de dados para a criação do objeto Cliente
    """
    

    dados = []

    caminho_json = 'clientes.json' #Nomeia arquivo JSON
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    print("================================================================\n          ---- Seja bem-vindo a tela de cadastro! ----\n================================================================")
    while True:
        nome_cliente = input('----------------------------\n  Insira seu nome: ')
        if validador_nome(nome_cliente):
            break
    while True:
        email_cliente = input('----------------------------\n  Insira seu email (Exemplo: cleyton@gmail.com):').lower().strip()
        if validador_email(email_cliente, dados):
            break

    while True:
        senha_cliente = pwinput.pwinput(prompt='----------------------------\n  Insira sua senha (Ela deve incluir pelo menos 10 caractéres, uma letra maiúscula e dois número):', mask = '*')
        confirm_senha = pwinput.pwinput(prompt='----------------------------\n  Insira sua senha novamente:', mask = '*')
        if validador_senha(senha_cliente, confirm_senha):
            break
    
    print('Cadastro realizado com sucesso.')
    validado = True
    if validado: #Checa se todos os valores insiredos são válidos
        print('-- Cadastro realizado com sucesso! --')
        clientes_json = Clientes(nome_cliente, email_cliente, senha_cliente) #Cria objeto

        dados.append(clientes_json.criador_dic()) #Adiciona dados ao arquivo

        with open(caminho_json, 'w', encoding='utf-8') as f: #Salva dados alterados
            json.dump(dados, f, indent = 4, ensure_ascii= False)