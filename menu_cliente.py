from crud_geral import CRUD
from pesquisa import pesquisa_cliente
banco_dados = []
id_usuario = None
caminho = 'bancos_json/clientes.json'
caminho_restaurantes = "bancos_json/restaurantes.json"
caminho_cardapio = "bancos_json/cardapio.json"

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
    banco_dados = CRUD.atualizar_dados()
    
    for usuario in banco_dados:
        if usuario.get('id') == id_usuario:
            usuario['alergia'] = usuario_encontrado['alergia'] 
            CRUD.salvar_dados(banco_dados)
            break 
        
    mostrar_perfil(usuario_encontrado)

def adicionar_cidade(usuario_encontrado):
    """
    - Adiciona ou atualiza a cidade do restaurante do usuário.

    Parâmetro:
     - usuario_encontrado (dict): Dicionário do usuário logado.
    """
    if 'cidade' not in usuario_encontrado:
        usuario_encontrado['cidade'] = ""

    dados_novos = input("Digite a cidade onde seu restaurante reside: ")
    CRUD.atualizar_usuario(usuario_encontrado, 'cidade', dados_novos)

    print("Cidade adicionada com sucesso!")
    mostrar_perfil(usuario_encontrado)
        
    CRUD.salvar_dados(banco_dados)
    CRUD.mostrar_perfil(usuario_encontrado)



def editar_perfil(usuario_encontrado):
    """
    - Permite ao usuário editar informações do seu perfil, como nome, senha, alergias, cidade ou excluir conta.
    
    Parâmetro:
     usuario_encontrado (dict): dicionário com os dados do usuário logado.
    """
    print("------ EDIÇÃO DE PERFIL ------")
    
    print("Deseja modificar qual informação: ")
    print("\n1. Nome \n2. Senha \n3. Alergias \n4. Cidade \n5. Apagar conta \n6. Sair")
    opc = int(input("> "))

    if opc == 1:
        CRUD.atualizar_nome(usuario_encontrado)
    elif opc == 2:
        CRUD.atualizar_senha(usuario_encontrado)
    elif opc == 3:
        adicionar_alergia(usuario_encontrado)
    elif opc == 4:
        adicionar_cidade(usuario_encontrado)
    elif opc == 5:
        CRUD.apagar_conta(usuario_encontrado)
    elif opc == 6:
        print("Saindo . . .")
        menu_cliente(usuario_encontrado)
    else:
        print("Opção inválida.")


def mostrar_perfil(usuario_encontrado):
    """
    - Exibe o perfil do usuário com nome, email, alergias e cidade.
    - Permite redirecionar para a edição de perfil ou retornar ao menu principal.
    
    Parâmetro:
    - usuario_encontrado: dicionário com os dados do usuário logado.
    """
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
    """
    - Exibe o menu principal para o cliente com opções de perfil, pesquisa ou biblioteca.
    
    Parâmetro:
    - usuario_encontrado: dicionário com os dados do usuário logado.
    """
    execucao = True
    while execucao:
        print(f"Bem vindo ao AllerGenie, {usuario_encontrado.get('nome')}!\n")
        print("Pressione o número referente a alguma dessas abas: ")
        print("1. Perfil \n2. Pesquisa \n3. Biblioteca\n")
        tecla = int(input("> "))

        if tecla not in [1, 2, 3]:
            print("\nErro: Pressione um número válido\n")
        elif tecla == 1:
            mostrar_perfil(usuario_encontrado)
        elif tecla == 2:
            pesquisa_cliente(usuario_encontrado)
            menu_cliente(usuario_encontrado)
        elif tecla == 3:
            print("bliblibliblib")