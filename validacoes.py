import hashlib

def validador_nome(nome):
    if nome != str(nome): #Verifica se o dado inserido é válido
        print('Erro: Tipo de dado inserido é inválido. Utilize apenas Strings.')
        return False
    elif len(nome) == 0 or len(nome.strip()) == 0: #Verifica se o nome está vazio
        print('Erro: Nome não pode estar vazio.')
        return False
    return True

def validador_cnpj(opc, cnpj, dados):
    if opc:
        for usuario in dados:
            if usuario.get('cnpj') == cnpj:
                print('Erro: CNPJ já cadastrado. Remova o CNPJ de sua conta anterior para adicioná-lo ao novo cadastro.')
                return False 
        if not cnpj.isdigit(): #Verifica se, ainda que String, os caractéres inseridos são números
            print('Erro: Caractére utilizado não é valido')
            return False
        elif cnpj != cnpj.strip(): #Verifica se algum espaço foi inserido
            print('Erro: Não são permitidos espaços')
            return False
        elif len(cnpj) != 14: #Verifica o número de letras do CNPJ
            print('Erro: Número de caractéres está incorreto')
            return False
        return True


def validador_email(email, dados):
    dominios_val = ['gmail', 'hotmail', 'outlook', 'yahoo'] #Lista de domínios válidos
    encontrado = False #Checador de presença de dominio
    for dominio in dominios_val: #Verifica elemento por elemento na lista
        if dominio in email: #Verifica se o elemento está na variável
            encontrado = True
            break
        
    for usuario in dados:
        if usuario.get('email') == email:
            print('Erro: Email já cadastrado.')
            return False
    if email == '' or len(email.strip()) == 0: #Verifica se o email está vázio
        print('Erro: Email não pode estar vázio.')
        return False
    elif '@' not in email or not email.endswith('.com'): #Verifica se o formato de emails está sendo seguido
        print('Erro: Insira um formato de email válido.')
        return False
    elif not encontrado: #Caso não possua domínio valido
        print('Erro: Insira um dominio válido.(gmail, hotmail, yahoo ou outlook)')
        return False
    return True

def validador_senha(senha_1, senha_2):
    contador_num = 0
    for caractere in senha_1:
        if caractere.isdigit():
            contador_num += 1
    if senha_1 == '' or len(senha_1.strip()) == 0: #Verifica se a senha foi preenchida ou não
        print('Erro: Senha não pode estar vázia')
        return False
    elif len(senha_1) < 10: #Verifica tamanho da senha
        print('Erro: Senha deve conter no mínimo 10 caractéres.')
        return False
    elif senha_1.lower() == senha_1: #Verifica se a senha usou apenas letras minúsculas
        print('Erro: Senha deve incluir pelo menos 1 letra maiúscula')
        return False
    elif senha_1 != senha_2: #Verifica se a primeira inserção da senha é igual a segunda
        print('Erro: Senha não pode ser diferente da confirmação da senha.')
        return False
    if contador_num < 2:
        print('Erro: Senha deve conter no mínimo 2 dígitos')
    return True

def criptografador(palavra_passe):
    """
    Criptografa o novo valor inserido para um aleatório em Secura Hash Algorithm de 256 bits

    """
    return hashlib.sha256(palavra_passe.encode()).hexdigest()