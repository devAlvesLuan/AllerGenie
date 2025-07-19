import hashlib

def validador_nome(nome):
    """
    - Valida se o nome inserido é uma string não vazia e sem apenas espaços.

    Parâmetro:
    - nome: dado inserido para validação do nome.

    Retorne:
    - True se válido, False se inválido.
    """
    if nome != str(nome):  # Verifica se o dado inserido é válido
        print('Erro: Tipo de dado inserido é inválido. Utilize apenas Strings.')
        return False
    elif len(nome) == 0 or len(nome.strip()) == 0:  # Verifica se o nome está vazio
        print('Erro: Nome não pode estar vazio.')
        return False
    return True


def validador_cnpj(opc, cnpj, dados):
    """
    - Valida o CNPJ inserido, verificando duplicidade, formatação e comprimento.

    Parâmetro:
    - opc: booleano que define se deve ou não realizar a validação.
    - cnpj: número de CNPJ em string.
    - dados: lista de dicionários com os dados dos usuários existentes.

    Retorne:
    - True se válido, False se inválido.
    """
    if opc:
        for usuario in dados:
            if usuario.get('cnpj') == cnpj:
                print('Erro: CNPJ já cadastrado. Remova o CNPJ de sua conta anterior para adicioná-lo ao novo cadastro.')
                return False
        if not cnpj.isdigit():  # Verifica se contém apenas números
            print('Erro: Caractére utilizado não é válido.')
            return False
        elif cnpj != cnpj.strip():  # Verifica espaços
            print('Erro: Não são permitidos espaços.')
            return False
        elif len(cnpj) != 14:  # Verifica tamanho
            print('Erro: Número de caractéres está incorreto.')
            return False
        return True


def validador_email(email, dados):
    """
    - Valida o email inserido, verificando domínio válido, duplicidade e formato correto.

    Parâmetro:
    - email: endereço de email a ser validado.
    - dados: lista de dicionários com os dados dos usuários existentes.

    Retorne:
    - True se válido, False se inválido.
    """
    dominios_val = ['gmail', 'hotmail', 'outlook', 'yahoo']
    encontrado = False

    for dominio in dominios_val:
        if dominio in email:
            encontrado = True
            break

    for usuario in dados:
        if usuario.get('email') == email:
            print('Erro: Email já cadastrado.')
            return False

    if email == '' or len(email.strip()) == 0:
        print('Erro: Email não pode estar vázio.')
        return False
    elif '@' not in email or not email.endswith('.com'):
        print('Erro: Insira um formato de email válido.')
        return False
    elif not encontrado:
        print('Erro: Insira um domínio válido. (gmail, hotmail, yahoo ou outlook)')
        return False

    return True


def validador_senha(senha_1, senha_2):
    """
    - Valida se a senha atende aos critérios de segurança: tamanho, maiúscula, dígitos e confirmação.

    Parâmetro:
    - senha_1: senha original.
    - senha_2: confirmação da senha.

    Retorne:
    - True se válido, False se inválido.
    """
    contador_num = 0
    for caractere in senha_1:
        if caractere.isdigit():
            contador_num += 1

    if senha_1 == '' or len(senha_1.strip()) == 0:
        print('Erro: Senha não pode estar vázia.')
        return False
    elif len(senha_1) < 10:
        print('Erro: Senha deve conter no mínimo 10 caractéres.')
        return False
    elif senha_1.lower() == senha_1:
        print('Erro: Senha deve incluir pelo menos 1 letra maiúscula.')
        return False
    elif senha_1 != senha_2:
        print('Erro: Senha não pode ser diferente da confirmação da senha.')
        return False
    elif contador_num < 2:
        print('Erro: Senha deve conter no mínimo 2 dígitos.')
        return False

    return True

def criptografador(palavra_passe):
    """
    Criptografa o novo valor inserido para um aleatório em Secura Hash Algorithm de 256 bits

    """
    return hashlib.sha256(palavra_passe.encode()).hexdigest()