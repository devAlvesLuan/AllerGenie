import json
import os
import keyboard
import hashlib
char_especial = ['!','@','#','$','%','^','&','*','(',')','-','+','?','_','=',',','<','>','/','"', '\'','\\'] #Adicionar checador de caractére espcial

def criptografador(palavra_passe): #Criptografado o novo valor inserido para um aleatório em Secura Hash Algorithm de 256 bits
    return hashlib.sha256(palavra_passe.encode()).hexdigest()

class Restaurante:
    def __init__(self, nome_completo, email, senha_1): #Adiciona atributos às instâncias
        self.nome_restaurante = nome_restaurante 
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
                  
    def validador(nome_restaurante, email, senha_1):
        if nome_restaurante != str(nome_restaurante): #Verifica se o dado inserido é válido
            print('Erro: O tipo de dado inserido é inválido. Utilize apenas Strings para o nome do restaurante.')
            return False
        elif len(nome_restaurante) == 0 or len(nome_restaurante.strip()) == 0: #Verifica se o nome está vazio
            print('Erro: O nome do restaurante não pode estar vazio.')
            return False



        if email != str(email): #Verifica se o dado inserido é válido
            print('Erro: O tipo de dado inserido é inválido. Utilize apenas Strings para o nome do restaurante.')
            return False
        elif '@' not in email or not email.endswith('.com'): #Verifica se o formato de emails está sendo seguido
            print('Erro: Insira um formato de email válido.')
            return False
        
        if len(senha_1) < 10: #Verifica tamanho da senha
            print('Erro: Senha deve conter no mínimo 10 caractéres.')
            return False
        elif senha_1.lower() == senha_1: #Verifica se a senha usou apenas letras minúsculas
            print('Erro: Senha deve incluir pelo menos 1 letra maiúscula')
            return False
        elif senha_1 == '': #Verifica se a senha foi preenchida ou não
            print('Erro: Senha não pode estar vázia')
            return False
        
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

    insert_2 = False
    execucao_1 = True
    execucao_2 = True

    while execucao_2: #Executado enquanto o código não encontrar um cadastro válido
        insert_1 = input('----------------------------\n  Insira o nome da empresa:')
        print('----------------------------\n  Incluir CNPJ? (Opcional)\n 1. Sim\n 2. Não')
        while execucao_1:
            evento = keyboard.read_event()#Consertar o seu buffer no loop while
            keyboard.clear_all_hotkeys()

            if evento.event_type == keyboard.KEY_DOWN: #Captura qual tecla foi pressionada
                chave = evento.name

                if chave == '2': #Realiza a checagem de se a tecla pressionada é válida ou não e qual a opção selecionada
                    insert_2 = False
                    execucao_1 = False
                    break
                elif chave == '1':
                    insert_2 = True
                    execucao_1 = False
                    break
                else:
                    print('Erro: Inserção inválida')

        if insert_2: #Checa se o usuário quer inserir CNPJ ou não
            insert_3 = input('----------------------------\n  insira seu CNPJ:')
        else:
            insert_3 = 'Não cadastrado.'
        insert_4 = input('----------------------------\n  Insira seu email (Exemplo: Cleyton@gmail.com):')
        insert_5 =input('----------------------------\n  insira sua senha (Pelo menos 10 caractéres e incluir pelo menos uma letra maiúscula, um caractére especial e um número):')
        

        if validador(insert_1, insert_2, insert_3, insert_4, insert_5): #Checa se todos os valores insiredos são válidos
            print('Cadastro realizado com sucesso.')
            restaurant = Restaurante(insert_1, insert_2, insert_3, insert_4, insert_5) #Cria objeto
            dados = []
            
            caminho_json = 'restaurantes.json' #Nomeia arquivo JSON

            if os.path.exists(caminho_json): #Acessa JSON existente e começa a edita-lo
                with open(caminho_json, 'r', encoding='utf-8') as f:
                    dados = json.load(f)

            dados.append(restaurant.criador_dic()) #Adiciona dados ao arquivo

            with open(caminho_json, 'w', encoding='utf-8') as f: #Salva dados alterados
                json.dump(dados, f, indent = 4, ensure_ascii= False)

            execucao_2 = False #Finaliza processo while