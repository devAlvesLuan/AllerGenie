import json
from menu_cliente import menu_cliente
caminho_restaurantes = 'banco_json/restaurante.json'
caminho_cardapio = 'banco_json/cardapio.json'

def ler_dados_json():
        """
        - Lê os dados dos arquivos JSON contendo informações dos restaurantes e cardápios.
        
        Retorne:
        - Uma tupla contendo dois elementos: (dados_restaurante, dados_cardapio)
        """
        with open(caminho_restaurantes, 'r', encoding='utf-8') as file:
            dados_restaurante =  json.load(file)
        with open(caminho_cardapio, 'r', encoding='utf-8') as file:
            dados_cardapio = json.load(file)
            
        return dados_restaurante, dados_cardapio

def pesquisa_geral(pesquisa, campo):
    """
    - Realiza a busca por um campo específico (como nome, cidade ou palavra-chave) dentro dos dados de restaurante.
    - Mostra os resultados com nome, cidade, palavras-chave e descrição do restaurante.

    Parâmetro:
    - pesquisa: termo que será buscado.
    - campo: campo do dicionário onde será feita a busca (ex: 'nome', 'cidade').

    Retorne:
    - Lista de tuplas com os resultados encontrados.
    """
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


def visualizar_restaurante(pesquisa, campo):
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

    i = 0
    if resultados:
        print("----------------------------------------------------------")
        for i, nome_restaurante, cidade, palavras_chave, descricao in resultados:
            print(f'{i+1}.\n')
            print(f"||> Nome restaurante: {nome_restaurante}")
            print(f"||> Cidade: {cidade}")
            print(f"||> Palavras-chave: {palavras_chave}")
            print(f"||> Descrição: {descricao}")
            print("----------------------------------------------------------")
    else:
        print("\nNada encontrado . . .")
    
    if i == 1:
        print("Deseja conhecer esse restaurante?\n1.Sim\n 2.Não")
        opc = int(input("> "))
    
    elif i > 1:
        print("Deseja conhecer algum desses restaurantes?\n1.Sim \n2.Não")
        opc = int(input("> "))
        if opc == 1:
            print()
        if opc == 'x':
            print
            
        

def pesquisa_prato(pesquisa):
    """
    - Realiza a busca de pratos nos cardápios dos restaurantes.
    - Exibe o nome do restaurante, prato, descrição e preço.

    Parâmetro:
    - pesquisa: termo que será comparado com o nome dos pratos.

    Retorne:
    - Lista de tuplas com os resultados encontrados.
    """
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
       


def pesquisa_cliente(usuario_encontrado):
    """
    - Menu de pesquisa para o cliente.
    - Permite escolher entre pesquisa por palavra-chave, prato, localização ou nome do restaurante.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do usuário logado.
    """
    print("\n------------------ Bem-vindo a guia de pesquisa! ------------------\n")
    print("Como deseja pesquisar?")
    print("\n1. Palavras-chave \n2. Pratos \n3. Localização \n4. Restaurantes \n5. Sair")
    opc = str(input("> "))

    if opc == '1':
        print("Digite as palavras: ")
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'palavra-chave')
        pesquisa_cliente(usuario_encontrado)
    elif opc == '2':
        print("Digite o que deseja: ")
        pesquisa = input("> ")
        pesquisa_prato(pesquisa)
        pesquisa_cliente(usuario_encontrado)
    elif opc == '3':
        print("Digite a localização: ")
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'cidade')
        pesquisa_cliente(usuario_encontrado)
    elif opc == '4':
        print("Digite o restaurante: ")
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'nome')
        pesquisa_cliente(usuario_encontrado)
    elif opc == '5':
        print('Saindo . . .')
        menu_cliente(usuario_encontrado)
