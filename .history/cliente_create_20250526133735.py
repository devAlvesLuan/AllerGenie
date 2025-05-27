import json
import os
import hashlib

def criptografador(palavra_passe):
    return hashlib.sha256(palavra_passe.encode()).hexdigest()

    """
    Criptografa o novo valor inserido para um aleatório em Secura Hash Algorithm de 256 bits

    """

class Clientes:
    def __init__(self, nome_cliente, email, senha_1, senha_2): #Adiciona atributos às instâncias
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
    def validador(nome_cliente, email, senha_1, senha_2):

        if nome_cliente != str(nome_cliente): #Verifica se o dado inserido é válido
            print('Erro: O tipo de dado inserido é inválido. Utilize apenas Strings para o nome do restaurante.')
            return False
        elif len(nome_cliente) == 0 or len(nome_cliente.strip()) == 0: #Verifica se o nome está vazio
            print('Erro: O nome do cliente não pode estar vazio.')
            return False


        if email != str(email): #Verifica se o dado inserido é válido
            print('Erro: O tipo de dado inserido é inválido. Utilize apenas Strings para o nome do restaurante.')
            return False
        elif '@' not in email or not email.endswith('.com'): #Verifica se o formato de emails está sendo seguido
            print('Erro: Insira um formato de email válido.')
            return False
        
        contador_num = 0
        for caractere in senha_1:
            if caractere.isdigit():
                contador_num += 1

        if len(senha_1) < 10: #Verifica tamanho da senha
            print('Erro: Senha deve conter no mínimo 10 caractéres.')
            return False
        elif senha_1.lower() == senha_1: #Verifica se a senha usou apenas letras minúsculas
            print('Erro: Senha deve incluir pelo menos 1 letra maiúscula')
            return False
        elif senha_1 != senha_2: #Verifica se a primeira inserção da senha é igual a segunda
            print('Erro: Senha não pode ser diferente da confirmação da senha.')
            return False
        elif senha_1 == '' or len(senha_1.strip()) == 0: #Verifica se a senha foi preenchida ou não
            print('Erro: Senha não pode estar vázia')
            return False
        elif contador_num < 2: #Verifica se a senha tem no mínimo 2 dígitos
            print('Erro: Senha deve conter no mínimo 2 dígitos.')

        dominios_val = ['gmail', 'hotmail', 'outlook', 'yahoo'] #Lista de domínios válidos
        encontrado = False #Checador de presença de dominio

        for dominio in dominios_val: #Verifica elemento por elemento na lista
            if dominio in email: #Verifica se o elemento está na variável
                encontrado = True
                break
        
        if not encontrado: #Caso não possua dominio valido
            print('Erro: Insira um dominio válido.(gmail, hotmail, yahoo ou outlook)')
            return False

        return True


    print("================================================================\n          ---- Seja bem-vindo a tela de cadastro! ----\n================================================================")

    execucao_cadastro = True

    while execucao_cadastro: #Executado enquanto o código não encontrar um cadastro válido
        nome_cliente = input('----------------------------\n  Insira o nome do cliente:')
        email_cliente = input('----------------------------\n  Insira seu email (Exemplo: Cleyton@gmail.com):')
        senha_cliente = input('----------------------------\n  insira sua senha (Ela deve incluir pelo menos 10 caractéres, uma letra maiúscula e dois número):')
        confirm_senha = input('----------------------------\n  Insira sua senha novamente:', mask = '*')

        if validador(nome_cliente, email_cliente, senha_cliente, confirm_senha): #Checa se todos os valores insiredos são válidos
            print('-- Cadastro realizado com sucesso! --')
            clientes_json = Clientes(nome_cliente, email_cliente, senha_cliente, confirm_senha) #Cria objeto
            dados = []

            caminho_json = 'clientes.json' #Nomeia arquivo JSON

            if os.path.exists(caminho_json): #Acessa JSON existente e começa a edita-lo
                with open(caminho_json, 'r', encoding='utf-8') as f:
                    dados = json.load(f)

            dados.append(clientes_json.criador_dic()) #Adiciona dados ao arquivo

            with open(caminho_json, 'w', encoding='utf-8') as f: #Salva dados alterados
                json.dump(dados, f, indent = 4, ensure_ascii= False)

            execucao_cadastro = False #Finaliza processo while