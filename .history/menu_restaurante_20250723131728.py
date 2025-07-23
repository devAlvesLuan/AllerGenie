import json
import pwinput
from validacoes import *
from cardapio_rest import cardapio
from crud_geral import CRUD, CrudRestaurante
    
def editar_perfil(usuario_encontrado):
    """
    - Exibe o menu de edição de perfil e direciona para a função correspondente com base na escolha do usuário.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    print("------ EDIÇÃO DE PERFIL ------")
    
    print("Deseja modificar qual informação: ")
    print("\n1. Nome \n2. Senha \n3. Cidade \n4. Palavras-Chaves \n5. Descrição  \n6. Apagar Conta \n7. Sair")
    opc = int(input("> "))

    if opc == 1:
        CRUD.atualizar_nome(usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 2:
        CRUD.atualizar_senha(usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 3:
        CRUD.adicionar_cidade(usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 4:
        CrudRestaurante.adicionar_palavraChave(usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 5:
        CrudRestaurante.adicionar_descricao(usuario_encontrado)
        mostrar_perfil(usuario_encontrado)
    elif opc == 6:
        CRUD.apagar_conta(usuario_encontrado)
        
    elif opc == 7:
        print("Saindo . . .")
        menu_empresa(usuario_encontrado)
    else:
        print("Opção inválida.")


def mostrar_perfil(usuario_encontrado):
    """
    - Exibe as informações do perfil do restaurante e oferece a opção de editar ou sair.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    execucao = True
    print("------ PERFIL ------")
    print("\nRestaurante: ", usuario_encontrado.get('nome'))
    print("Email: ", usuario_encontrado.get('email'))
    print("CNPJ: ", usuario_encontrado.get('cnpj'))
    print("Cidade: ", usuario_encontrado.get('cidade', 'Não inserido.'))
    print("Palavras-Chaves: ", usuario_encontrado.get('palavra-chave', 'Não inserido.'))
    print("Descrição: ", usuario_encontrado.get('descricao', 'Não inserido.'))
    media_restaurante = usuario_encontrado.get('avaliacao', {}).get('media')
    
    if media_restaurante is None or media_restaurante == 0.0:
        print("Avaliação: Sem avaliações.")
    else:
        print(f"Avaliação: {media_restaurante:.1f}")
    
    while execucao:
        print("\n1. Editar Perfil \n2. Sair")
        opc = int(input("> "))
        
        if opc not in [1,2]:
            print("Erro: opção inválida.")
            
        if opc == 1:
            print("REALIZANDO EDIÇÃO")
            editar_perfil(usuario_encontrado)
            execucao = False
        elif opc == 2:
            print("SAINDO. . .")
            menu_empresa(usuario_encontrado)
            execucao = False


def menu_empresa(usuario_encontrado):
    """
    - Exibe o menu principal do restaurante com acesso ao perfil e cardápio.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    execucao = True
    while execucao:
        print(f"Bem vindo ao AllerGenie, {usuario_encontrado.get('nome')}!\n")
        print("Pressione o número referente a algum dessas abas: ")
        print("1. Perfil \n2. Cárdapio")
        tecla = str(input("> "))

        if tecla not in ['1', '2']:
            print("\nErro: Pressione um número válido\n")
            continue

        if tecla == '1':
            mostrar_perfil(usuario_encontrado)
            execucao = False  
            break
        elif tecla == '2':
            cardapio(usuario_encontrado)
