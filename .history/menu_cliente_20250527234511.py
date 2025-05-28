import json
import pwinput
from validacoes import *
from start_page import main 

banco_dados = []
id_usuario = None
caminho = 'clientes.json'
caminho_restaurantes = "restaurantes.json"
caminho_cardapio = "cardapio.json"



def apagar_conta(usuario_encontrado):
    """
    - Exclui a conta do usuário após confirmação de credenciais e confirmação textual.

    Parâmetro:
        usuario_encontrado (dict): Dicionário contendo os dados do usuário logado.
    """
    id_usuario = usuario_encontrado.get('id')

    exc = True
    print("Deseja continuar e deletar sua conta? ")
    print("\n1. Sim \n2. Não")
    opc = int(input("> "))
    
    if opc == 1:
        while exc:
            email = input("Digite seu email (Digite 2 para voltar para edição de perfil): ")
            if email != '2':
                senha = pwinput.pwinput(prompt='Digite sua senha: ', mask = '*')
                banco_dados = atualizar_dados()
                if usuario_encontrado.get('email') == email and usuario_encontrado.get('senha') == criptografador(senha):
                    conferir = input("Escreva 'Confirmo' para confirmar a exclusão da sua conta: ").lower().strip()
            
                    if conferir == 'confirmo':
                        for usuario in banco_dados:
                            if usuario.get('id') == id_usuario:
                                banco_dados.remove(usuario)
                                break
                        
                        salvar_dados(banco_dados)
                        main()
                    else:
                        print('Inserção inválida')
                else:
                    print("Tente novamente")
            elif email == '2':
                editar_perfil(usuario_encontrado)
            else:
                print('Inserção inválida')
    elif opc == 2:
        print("Voltando para a edição de perfil. . .")
        editar_perfil(usuario_encontrado)
    else: 
        print("Inserção inválida")
        

def atualizar_dados():
    """
    Lê e retorna os dados do arquivo JSON.

    Returns:
        list: Lista de usuários armazenados no arquivo JSON.
    """
    with open(caminho, 'r', encoding='utf-8') as file:
        return json.load(file)

def salvar_dados(banco_dados):
    """
    Salva os dados atualizados no arquivo JSON.

    Args:
        banco_dados (list): Lista de usuários atualizada.
    """
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco_dados, f, indent=4, ensure_ascii=False)

def atualizar_usuario(usuario_encontrado, campo, dados_novos):
    """
    - Atualiza um campo específico do usuário.

    Args:
        usuario_encontrado (dict): Dicionário do usuário logado.
        campo (str): Campo que será atualizado.
        dados_novos (str): Novo valor para o campo.

    Returns:
        list: Lista atualizada com os dados modificados.
    """
    banco_dados = atualizar_dados()
    id_usuario = usuario_encontrado.get('id')
    
    for usuario in banco_dados:
        if usuario.get('id') == id_usuario:
            usuario[campo] = dados_novos
            usuario_encontrado[campo] = dados_novos
            salvar_dados(banco_dados)
            break  

    return banco_dados

def atualizar_nome(usuario_encontrado):
    """
    - Atualiza o nome do usuário, com verificação de entrada e opção de voltar.

    Args:
        usuario_encontrado (dict): Dicionário do usuário logado.
    """
    while True:
        dados_novos = input("Atualize seu nome: (Digite 2 para voltar)")
        if validador_nome(dados_novos):
            break
        elif dados_novos == '2':
            print("Voltando para a edição de perfil. . .")
            editar_perfil(usuario_encontrado)
    
    atualizar_usuario(usuario_encontrado, 'nome', dados_novos)
    mostrar_perfil(usuario_encontrado)

def atualizar_senha(usuario_encontrado):
    """
    - Atualiza a senha do usuário após verificação de email e senha atual.
    
    Args:
        usuario_encontrado (dict): Dicionário do usuário logado.
    """
    atualizando = True
    while atualizando:
        print('Confirme que é você. (Digite 2 para voltar.)')
        email = input("Digite seu email: ")
        if email != '2':
            senha = pwinput.pwinput(prompt='Digite sua senha: ', mask = '*')
            if usuario_encontrado.get('email') == email and usuario_encontrado.get('senha') == criptografador(senha):
                while True:
                    dados_novos = pwinput.pwinput(prompt="Atualize sua senha (Digite 2 para voltar): ", mask = '*')
                    if dados_novos != '2':
                        confirmacao = pwinput.pwinput(prompt="Digite sua senha novamente: ", mask = '*')
                        if validador_senha(dados_novos, confirmacao):
                            atualizar_usuario(usuario_encontrado, 'senha', criptografador(dados_novos))
                            print("Senha modificada com sucesso!")
                            mostrar_perfil(usuario_encontrado)
                    elif dados_novos == '2':
                        print("Voltando para a edição de perfil. . .")
                        editar_perfil(usuario_encontrado)
                
            else:
                print("Login inválido. Insira dados novamente ou retorne a edição de perfil inserindo '0'.")
        elif email == '2':
            print("Voltando para a edição de perfil. . .")
            editar_perfil(usuario_encontrado)
        else:
            print('Inserção inválida')

def adicionar_alergia(usuario_encontrado):
    """
    - Adiciona ou atualiza as alergias do usuário no perfil.

    Parâmetro:
        usuario_encontrado (dict): Dicionário do usuário logado.
    """
    if 'alergia' not in usuario_encontrado:
        usuario_encontrado['alegia'] = ""
    
    dados_novos = input("Digite sua(s) alergia(s): ")
    usuario_encontrado['alergia'] = dados_novos
    banco_dados = atualizar_dados()
    
    for usuario in banco_dados:
        if usuario.get('id') == id_usuario:
            usuario['alergia'] = usuario_encontrado['alergia'] 
            salvar_dados(banco_dados)
            break 
        
    mostrar_perfil(usuario_encontrado)

def adicionar_cidade(usuario_encontrado):
    """
    - Adiciona ou atualiza a cidade do restaurante do usuário.

    Parâmetro:
        usuario_encontrado (dict): Dicionário do usuário logado.
    """
    if 'cidade' not in usuario_encontrado:
        usuario_encontrado['cidade'] = ""

    dados_novos = input("Digite a cidade onde seu restaurante reside: ")
    atualizar_usuario(usuario_encontrado, 'cidade', dados_novos)

    print("Cidade adicionada com sucesso!")
    mostrar_perfil(usuario_encontrado)
        
    salvar_dados(banco_dados)
    mostrar_perfil(usuario_encontrado)



def editar_perfil(usuario_encontrado):
    print("------ EDIÇÃO DE PERFIL ------")
    
    print("Deseja modificar qual informação: ")
    print("\n1. Nome \n2. Senha \n3. Alergias \n4. Cidade \n5. Apagar conta \n6. Sair")
    opc = int(input("> "))

    if opc == 1:
        atualizar_nome(usuario_encontrado)
    elif opc == 2:
        atualizar_senha(usuario_encontrado)
    elif opc == 3:
        adicionar_alergia(usuario_encontrado)
    elif opc == 4:
        adicionar_cidade(usuario_encontrado)
    elif opc == 5:
        apagar_conta(usuario_encontrado)
    elif opc == 6:
        print("Saindo . . .")
        menu_cliente(usuario_encontrado)
    else:
        print("Opção inválida.")

    

def mostrar_perfil(usuario_encontrado):
    
    execucao = True
    print("------ PERFIL ------")
    print("\nNome: ", usuario_encontrado.get('nome'))
    print("Email: ", usuario_encontrado.get('email'))
    print("Alergias: ", usuario_encontrado.get('alergia','Não inserido.'))
    print("Cidade: ", usuario_encontrado.get('cidade','Não inserido.'))
    
    
    while execucao:
        print("\n1. Editar Perfil \n2. Sair")
        opc = int(input(""))
        
        if opc not in [1,2]:
            print("Erro: opção inválida.")
            
        if opc == 1:
            print("REALIZANDO EDIÇÃO")
            editar_perfil(usuario_encontrado)
            execucao = False
        elif opc == 2:
            print("SAINDO. . .")
            menu_cliente(usuario_encontrado)
            execucao = False

def menu_cliente(usuario_encontrado):
    execucao = True
    while execucao:
        print(f"Bem vindo ao AllerGenie, {usuario_encontrado.get('nome')}!\n")
        print("Pressione o número referente a alguma dessas abas: ")
        print("1. Perfil \n2. Pesquisa \n3. Biblioteca\n")
        tecla = int(input("> "))

        if tecla not in [1, 2, 3]:
            print("\nErro: Pressione um número válido\n")
            continue

        if tecla == 1:
            mostrar_perfil(usuario_encontrado)
            execucao = False  
            break
        elif tecla == 2:
            pesquisa_cliente(usuario_encontrado)

def ler_dados_json():
    with open(caminho_restaurantes, 'r', encoding='utf-8') as file:
        dados_restaurante =  json.load(file)
    with open(caminho_cardapio, 'r', encoding='utf-8') as file:
        dados_cardapio = json.load(file)
        
    return dados_restaurante, dados_cardapio



def pesquisa_geral(pesquisa, campo):
    dados_restaurantes,_ = ler_dados_json()

    resultados = []
    
    for dados in dados_restaurantes:
        dado_pedido = str(dados.get(campo))
        cidade = dados.get('cidade', '')
        palavras_chave = dados.get('palavra-chave', 'Não adicionada')
        nome_restaurante = dados.get('nome')
        descricao = dados.get('descricao', 'Não adicionada')
        if pesquisa.lower().strip() in dado_pedido.lower().strip():
            resultados.append((nome_restaurante, cidade, palavras_chave, descricao))

    if resultados:
        print("----------------------------------------------------------")
        for nome_restaurante, cidade, palavras_chave, descricao in resultados:
            print(f"||> Nome restaurante: {nome_restaurante}")
            print(f"||> Cidade: {cidade}")
            print(f"||> Palavras-chave: {palavras_chave}")
            print(f"||> Descrição: {descricao}")
            print("----------------------------------------------------------")
            
    else:
        print("\nNada encontrado . . .")
        
    pesquisa_cliente()
    return resultados

def pesquisa_prato(pesquisa):
    _, dados_cardapio = ler_dados_json()  
    resultados = []

    for nome_restaurante, pratos in dados_cardapio.items():
        for prato in pratos:
            nome_prato = prato.get('nome-prato')
            descricao = prato.get('descricao', 'Não encontrado')
            preco = prato.get('preco', 'Não encontrado')
            if pesquisa.lower().strip() in nome_prato.lower().strip():
                resultados.append((nome_restaurante, nome_prato, descricao, preco))
                
    if resultados:
        print("----------------------------------------------------------")
        for nome_restaurante, nome_prato, descricao, preco in resultados:
            print(f"||> Nome restaurante: {nome_restaurante}")
            print(f"||> Prato: {nome_prato}")
            print(f"||> Descrição: {descricao}")
            print(f"||> Preço: {preco}R$")
            print("----------------------------------------------------------")
    else:
        print("Nada encontrado . . .")
        
    pesquisa_cliente()
    return resultados

def pesquisa_cliente(usuario_encontrado):
    print("\n------------------ Bem-vindo a guia de pesquisa! ------------------\n")
    print("Como deseja pesquisar?")
    print("\n1. Palavras-chave \n2. Pratos \n3. Localização \n4. Restaurantes \n5. Sair")
    opc = str(input("> "))
    
    if opc == '1':
        print("Digite as palavras: ")
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'palavra-chave')
    elif opc == '2':
        print("Digite o que deseja: ")
        pesquisa = input("> ")
        pesquisa_prato(pesquisa)
    elif opc == '3':
        print("Digite a localização: ")
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'cidade')
    elif opc == '4':
        print("Digite o restaurante: ")
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'nome')
    elif opc == '5':
        print('Saindo . . .')
        menu_cliente(usuario_encontrado)