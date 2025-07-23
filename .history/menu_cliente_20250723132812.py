from crud_geral import *
from util import *
from pesquisa import pesquisa_cliente
from start_page import main
banco_dados = []
caminho = 'bancos_json/clientes.json'
caminho_restaurantes = "bancos_json/restaurantes.json"
caminho_cardapio = "bancos_json/cardapio.json"




def editar_perfil(usuario_encontrado):
    """
    - Permite ao usuário editar informações do seu perfil, como nome, senha, alergias, cidade ou excluir conta.
    
    Parâmetro:
     usuario_encontrado (dict): dicionário com os dados do usuário logado.
    """
    print(Utils.pinta("------ EDIÇÃO DE PERFIL ------", 'amarelo'))
    
    print("Deseja modificar qual informação: ")
    print("\n1. Nome \n2. Senha \n3. Alergias \n4. Cidade \n5. Apagar conta \n6. Sair")
    opc = int(input("> "))

    if opc == 1:
        CRUD.atualizar_nome('bancos_json/clientes.json', usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 2:
        CRUD.atualizar_senha('bancos_json/clientes.json', usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 3:
        CrudCliente.adicionar_alergia('bancos_json/clientes.json', usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 4:
        CRUD.adicionar_cidade('bancos_json/clientes.json', usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 5:
        CRUD.apagar_conta('bancos_json/clientes.json', usuario_encontrado)
        main()
    elif opc == 6:
        print(Utils.pinta('Saindo . . .', 'amarelo'))
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
    print(Utils.pinta("------ PERFIL ------", 'amarelo'))
    print("Nome: ", usuario_encontrado.get('nome'))
    print("Email: ", usuario_encontrado.get('email'))
    print("Alergias: ", usuario_encontrado.get('alergia','Não inserido.'))
    print("Cidade: ", usuario_encontrado.get('cidade','Não inserido.'))
    
    while execucao:
        print("\n1. Editar Perfil \n2. Sair")
        opc = int(input(""))
        
        if opc not in [1,2]:
            print("Erro: opção inválida.")
            
        if opc == 1:
            Utils.limpar_tela()
            print(Utils.pinta('- - -Realizando edição . . .', 'azul'))
            editar_perfil(usuario_encontrado)
            execucao = False
        elif opc == 2:
            Utils.limpar_tela()
            print(Utils.pinta('Saindo . . .', 'amarelo'))
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
        
        print(Utils.pinta(f"--- Bem vindo ao AllerGenie, {usuario_encontrado.get('nome')}! ---\n ", "ciano_claro"))
        print("Pressione o número referente a alguma dessas abas: ")
        print("1. Perfil \n2. Pesquisa \n3. Biblioteca\n")
        tecla = int(input("> "))

        if tecla not in [1, 2, 3]:
            print("\nErro: Pressione um número válido\n")
        elif tecla == 1:
            Utils.limpar_tela()
            mostrar_perfil(usuario_encontrado)
        elif tecla == 2:
            Utils.limpar_tela()
            pesquisa_cliente()
            menu_cliente(usuario_encontrado)
        elif tecla == 3:
            Utils.limpar_tela()
            print("bliblibliblib")