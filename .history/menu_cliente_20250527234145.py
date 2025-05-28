import json
caminho_restaurantes = "restaurantes.json"
caminho_cardapio = "cardapio.json"


def ler_dados_json():
    """
    Lê os dados dos arquivos JSON de restaurantes e cardápios.

    Returns:
        tuple: Contendo dois elementos:
            - dados_restaurante (list): Lista de restaurantes.
            - dados_cardapio (dict): Dicionário com cardápios por restaurante.
    """
    with open(caminho_restaurantes, 'r', encoding='utf-8') as file:
        dados_restaurante =  json.load(file)
    with open(caminho_cardapio, 'r', encoding='utf-8') as file:
        dados_cardapio = json.load(file)
        
    return dados_restaurante, dados_cardapio



def pesquisa_geral(pesquisa):
    """
    Realiza uma pesquisa geral entre localização, restaurante e pratos.

    Args:
        pesquisa (str): Texto a ser pesquisado.

    Returns:
        list: Lista de resultados encontrados.
    """
    resultados = []
    
    valor_localizacao = pesquisa_localizacao(pesquisa)
    valor_restaurante = pesquisa_restaurante(pesquisa)
    valor_prato = pesquisa_prato(pesquisa)
    
    if valor_localizacao:
        valor_encontrado = True
        resultados += valor_localizacao
    elif valor_restaurante:
        valor_encontrado = True
        resultados += valor_restaurante
    elif valor_prato:
        valor_encontrado = True
        resultados += valor_prato
        
    if resultados:
        print("-----------------------------")
        for itens in resultados:
              print(itens)       

    return resultados



def pesquisa_prato(pesquis):
    """
    Realiza pesquisa por nome de prato nos cardápios.

    Args:
        pesquisa (str): Nome (ou parte) do prato a ser buscado.

    Returns:
        list: Lista de tuplas contendo nome do restaurante, prato, descrição e preço.
    """
    _, dados_cardapio = ler_dados_json()  
    resultados = []

    for nome_restaurante, pratos in dados_cardapio.items():
        for prato in pratos:
            nome_prato = prato.get('nome-prato')
            descricao = prato.get('descricao', 'Não encontrado')
            preco = prato.get('preco', 'Não encontrado')
            if pesquisa.lower() in nome_prato.lower():
                resultados.append((nome_restaurante, nome_prato, descricao, preco))
     
    if resultados:
        print("-----------------------------")
        for nome_restaurante, nome_prato, descricao, preco in resultados:
            print(f"Nome restaurante: {nome_restaurante}")
            print(f"Prato: {nome_prato}")
            print(f"Descrição: {descricao}")
            print(f"Preço: {preco}R$")
            print("-----------------------------")
    else:
        print("Nada encontrado . . .")
    
    return resultados



def pesquisa_localizacao(pesquisa):
    """
    Realiza pesquisa por localização (cidade) nos dados de restaurantes.

    Args:
        pesquisa (str): Nome (ou parte) da cidade a ser buscada.

    Returns:
        list: Lista de tuplas com nome do restaurante, cidade e palavras-chave.
    """
    dados_restaurantes,_ = ler_dados_json()
    resultados = []
    
    for dados in dados_restaurantes:
        cidade = dados.get('cidade', '')
        palavras_chave = dados.get('palavra-chave', '')
        nome_restaurante = dados.get('nome')

        if pesquisa.lower() in cidade.lower():
            resultados.append((nome_restaurante, cidade, palavras_chave))

    if resultados:
        print("-----------------------------")
        for nome_restaurante, local, palavras_chave in resultados:
            print(f"Nome restaurante: {nome_restaurante}")
            print(f"Cidade: {local}")
            print(f"Palavras-chave: {palavras_chave}")
            print("-----------------------------")
    else:
        print("Nada encontrado . . .")
    
    return resultados



def pesquisa_restaurante(pesquisa):
    """
    Realiza pesquisa pelo nome do restaurante.

    Args:
        pesquisa (str): Nome (ou parte) do restaurante a ser buscado.

    Returns:
        list: Lista de tuplas com nome, cidade, palavras-chave e descrição do restaurante.
    """
    dados_restaurantes,_ = ler_dados_json()
    resultados = []
    
    for dados in dados_restaurantes:
        cidade = dados.get('cidade', '')
        palavras_chave = dados.get('palavra-chave', 'Não informado')
        nome_restaurante = dados.get('nome')
        descricao = dados.get('descricao', 'Não informado')

        if pesquisa.lower().strip() in nome_restaurante.lower().strip():
            resultados.append((nome_restaurante, cidade, palavras_chave, descricao))

    if resultados:
        print("-----------------------------")
        for nome_restaurante, cidade, palavras_chave, descricao in resultados:
            print(f"Nome restaurante: {nome_restaurante}")
            print(f"Cidade: {cidade}")
            print(f"Palavras-chave: {palavras_chave}")
            print(f"Descrição: {descricao}")
            print("-----------------------------")
    else:
        print("Nada encontrado . . .")
    
    return resultados



def pesquisa_cliente():
    """
    Menu de pesquisa para o cliente. 
    Permite escolher entre pesquisa geral, por prato, por localização ou por restaurante.
    """
    print("Bem-vindo a guia de pesquisa!")
    print("Como deseja pesquisar?")
    print("\n1. Pesquisa Geral \n2. Pratos \n3. Localização \n4. Restaurantes \n5. Sair")
    opc = str(input("> "))
    
    if opc == '1':
        print("Digite o que deseja: ")
        pesquisa = input("> ")
        pesquisa_geral(pesquisa)
    elif opc == '2':
        print("Digite o que deseja: ")
        pesquisa = input("> ")
        pesquisa_prato(pesquisa)
    elif opc == '3':
        print("Digite o que deseja: ")
        pesquisa = input("> ")
        pesquisa_localizacao(pesquisa)
    elif opc == '4':
        print("Digite o que deseja: ")
        pesquisa = input("> ")
        pesquisa_restaurante(pesquisa)
    elif opc == '5':
        print
