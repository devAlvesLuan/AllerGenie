from crud_geral import CRUD, CrudCliente
from pesquisa import pesquisa_cliente
from biblioteca import Biblioteca

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
    print("------ EDIÇÃO DE PERFIL ------")
    
    print("Deseja modificar qual informação: ")
    print("\n1. Nome \n2. Senha \n3. Alergias \n4. Cidade \n5. Apagar conta \n6. Sair")
    opc = int(input("> "))

    if opc == 1:
        CRUD.atualizar_nome(usuario_encontrado)
    elif opc == 2:
        CRUD.atualizar_senha(usuario_encontrado)
    elif opc == 3:
        CrudCliente.adicionar_alergia(usuario_encontrado)
    elif opc == 4:
        CRUD.adicionar_cidade(usuario_encontrado)
    elif opc == 5:
        CRUD.apagar_conta(usuario_encontrado)
    elif opc == 6:
        print("Saindo . . .")
        menu_client(usuario_encontrado)
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
            menu_client(usuario_encontrado)
            execucao = False


def menu_client(usuario_encontrado):
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
            pesquisa_cliente()
            menu_client(usuario_encontrado)
        elif tecla == 3:
            Biblioteca.menu_pessoal(usuario_encontrado)