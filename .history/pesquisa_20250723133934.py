import json
from crud_geral import CRUD
from util import*

caminho_restaurantes = 'bancos_json/restaurantes.json'
caminho_cardapio = 'bancos_json/cardapio.json'

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
        print(Utils.pinta("Nada encontrado . . .", 'vermelho'))


def visualizar_restaurante(pesquisa, campo):
    dados_restaurantes, dados_cardapio = ler_dados_json()

    resultados = []
    
    for dados in dados_restaurantes:
        dado_pedido = str(dados.get(campo))
        cidade = dados.get('cidade', '')
        palavras_chave = dados.get('palavra-chave', 'Não adicionada')
        nome_restaurante = dados.get('nome')
        descricao = dados.get('descricao', 'Não adicionada')
        if pesquisa.lower().strip() in dado_pedido.lower().strip():
            resultados.append((nome_restaurante, cidade, palavras_chave, descricao))

    i = 1
    if resultados:
        print("----------------------------------------------------------")
        for nome_restaurante, cidade, palavras_chave, descricao in resultados:
            print(f'{i}')
            print(f"||> Nome restaurante: {nome_restaurante}")
            print(f"||> Cidade: {cidade}")
            print(f"||> Palavras-chave: {palavras_chave}")
            print(f"||> Descrição: {descricao}")
            print("----------------------------------------------------------")
            
            i += 1
            
            
        print("Deseja conhecer algum desses restaurantes?\n1.Sim\n2.Não")
        opc = str(input("> "))
        
        if opc == '1':
            nome_escolhido = input("Digite o nome do restaurante que deseja conhecer: ").strip().lower()

            restaurante_encontrado = False
            
            for nome_restaurante, pratos in dados_cardapio.items():
                if nome_escolhido.strip().lower() in nome_restaurante.strip().lower():
                    restaurante_encontrado = True
                    nome_restaurante_encontrado = nome_restaurante
                    print(f"\nCardápio do restaurante: {nome_restaurante}")
                    for prato in pratos:
                        nome_prato = prato.get('nome-prato')
                        descricao = prato.get('descricao', 'Não encontrado')
                        preco = prato.get('preco', 'Não encontrado')

                        print("----------------------------------------------------------")
                        print(f"||> Prato: {nome_prato}")
                        print(f"||> Descrição: {descricao}")
                        print(f"||> Preço: {preco}R$")
                        print("----------------------------------------------------------")
                        
            acao = str(input('1. Avaliar Restaurante\n2. Comentarios\n3. Adicionar aos favoritos\n4. Sair\n> '))
            
            if acao == '1':
                avaliar_restaurante(nome_restaurante_encontrado)
            elif acao == '2':
                visualizar_cometarios(nome_restaurante_encontrado)
            elif acao == '3':
                print
            elif acao == '4':
                pesquisa_cliente()
                
                        

                if not restaurante_encontrado:
                    print("Restaurante não encontrado no cardápio.")
            
        elif opc == '2':
            return
    else:
       print(Utils.pinta("Nada encontrado . . .", 'vermelho'))

def avaliar_restaurante(restaurante):
    
    dados_restaurantes,_ = ler_dados_json()
    restaurante_encontrado = False
    for rest in dados_restaurantes:
        if rest['nome'].lower().strip() == restaurante.lower().strip():
            print(f'Qual nota deseja atribuir de 0-5 para o restaurante {restaurante}: ')
            avaliacao = float(input('> '))
            
            restaurante_encontrado = True
            if 0 <= avaliacao <= 5:
               
                rest["avaliacao"]["soma_avaliacoes"] += avaliacao
                rest["avaliacao"]["quantidade_avaliacoes"] += 1
                rest["avaliacao"]["media"] = (
                    rest["avaliacao"]["soma_avaliacoes"] / rest["avaliacao"]["quantidade_avaliacoes"]
                )
                CRUD.salvar_dados('bancos_json/restaurantes.json', dados_restaurantes)
                
                
                print("----------------------------------------------------------")
                print(Utils.pinta(f'Avaliação de {avaliacao} atribuída com sucesso ao restaurante {restaurante}!.', 'verde-claro'))
                print("----------------------------------------------------------")
                pesquisa_cliente()

            else:
                print('Avaliação inválida. Deve ser entre 0 e 5.')
                
        if restaurante_encontrado:
            CRUD.salvar_dados('bancos_json/restaurantes.json', dados_restaurantes)
              

def visualizar_cometarios(restaurante):
    banco_comentarios = CRUD.atualizar_dados('bancos_json/comentarios.json')
    
    if restaurante in banco_comentarios:
        print(f'\nComentarios para o restaurante {restaurante}\n')
        print("----------------------------------------------------------")
        comentarios_restaurante = banco_comentarios[restaurante]
        
        for usuario, comentarios in comentarios_restaurante.items():
            print(f"Usuário: {usuario}")
            for comentario in comentarios:
                print(f"- {comentario}")
            print("----------------------------------------------------------")
            
            
            
        print('Deseja fazer um comentário nesse restaurante?\n1. Sim \n2. Não (Retorna para o menu de pesquisa)')
        opc = str(input('> '))
        
        if opc == '1':
            fazer_comentario(restaurante)
        elif opc == '2':
            pesquisa_cliente()
        
        
        
    else:
        print(f"\nAinda não há comentários para o restaurante '{restaurante}'.\n")
        print('Deseja fazer um comentário nesse restaurante?\n1. Sim \n2. Não')
        opc = str(input('> '))
        
        if opc == '1':
            fazer_comentario(restaurante)
        elif opc == '2':
            pesquisa_cliente()
        
        
def fazer_comentario(restaurante):
    dados_usuarios_temp = CRUD.atualizar_dados('bancos_json/clientes.json')
    print("Digite seu email (será utilizado para encontrar seu nome de usuário):\n")
    email = str(input('> '))
    
    nome_usuario = None

    # Busca o nome do usuário pelo email
    for usuario in dados_usuarios_temp:
        if usuario.get('email') == email:
            nome_usuario = usuario.get('nome')
            break

    if not nome_usuario:
        print("Email não encontrado.")
        return
       
    print(f"Digite seu comentario, {nome_usuario}: ")
    comentario = str(input('> '))
    
    comentarios = CRUD.atualizar_dados('bancos_json/comentarios.json')
    
    if restaurante not in comentarios:
        comentarios[restaurante] = {}
    if nome_usuario not in comentarios[restaurante]:
        comentarios[restaurante][nome_usuario] = []
    
    comentarios[restaurante][nome_usuario].append(comentario)
    
    CRUD.salvar_dados('bancos_json/comentarios.json', comentarios)
    
    print(Utils.pinta("Comentário adicionado com sucesso!", 'verde_claro'))

        

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
            print(Utils.pinta(f"||> Nome restaurante: {nome_restaurante}", 'branco_brilhante'))
            print(Utils.pinta(f"||> Prato: {nome_prato}", 'branco_brilhante'))
            print(Utils.pinta(f"||> Descrição: {descricao}", 'branco_brilhante'))
            print(Utils.pinta(f"||> Preço: {preco}R$", 'branco_brilhante'))
            print("----------------------------------------------------------")
    else:
        print(Utils.pinta("Nada encontrado . . .", 'vermelho'))
       


def pesquisa_cliente():
    """
    - Menu de pesquisa para o cliente.
    - Permite escolher entre pesquisa por palavra-chave, prato, localização ou nome do restaurante.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do usuário logado.
    """
    print(Utils.pinta("\n------------------ Bem-vindo a guia de pesquisa! ------------------\n", 'verde_claro'))
    print("Como deseja pesquisar?")
    print("\n1. Palavras-chave \n2. Pratos \n3. Localização \n4. Restaurantes \n5. Sair")
    opc = str(input("> "))

    if opc == '1':
        print(Utils.pinta("Digite as palavras: ", 'ciano'))
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'palavra-chave')
        pesquisa_cliente()
    elif opc == '2':
        print(Utils.pinta("Digite o que deseja: ", 'ciano'))
        pesquisa = input("> ")
        pesquisa_prato(pesquisa)
        pesquisa_cliente()
    elif opc == '3':
        print(Utils.pinta("Digite a localização: ", 'ciano'))
        pesquisa = input("> ")
        pesquisa_geral(pesquisa, 'cidade')
        pesquisa_cliente()
    elif opc == '4':
        print(Utils.pinta("Digite o restaurante: ", 'ciano'))
        pesquisa = input("> ")
        visualizar_restaurante(pesquisa, 'nome')
        pesquisa_cliente()
    elif opc == '5':
        print(Utils.pinta('Saindo . . .', 'amarelo'))
        return
