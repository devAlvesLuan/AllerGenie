import json
import pwinput
from validacoes import *
from start_page import main
from cardapio_rest import cardapio

banco_dados = []
caminho = 'restaurantes.json'

def apagar_conta(usuario_encontrado):
    """
    - Realiza o processo de exclusão da conta do usuário, mediante confirmação por email, senha e validação textual.
    - Remove o usuário do banco de dados e retorna ao início do sistema, se confirmado.

    Parâmetro:
    - usuario_encontrado: dicionário contendo os dados do usuário logado.

    Retorne:
    - Nenhum
    """
    id_usuario = usuario_encontrado.get('id')
    exc = True
    print("Deseja continuar? ")
    print("\n1. Sim \n2. Não")
    opc = int(input("> "))

    if opc == 1:
        while exc:
            email = input("Digite seu email (Digite 2 para voltar para edição de perfil): ")
            if email != '2':
                senha = pwinput.pwinput(prompt='Digite sua senha: ', mask='*')
                banco_dados = atualizar_dados()
                if usuario_encontrado.get('email') == email and usuario_encontrado.get('senha') == criptografador(senha):
                    confir = input("Escreva 'Confirmo' para confirmar a exclusão da sua conta: ").lower().strip()

                    if confir == 'confirmo':
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
                    exc = True
            elif email == '2':
                editar_perfil(usuario_encontrado)
            else:
                print('Inserção inválida')
    elif opc == 2:
        print("Voltando para a edição de perfil. . .")
        editar_perfil(usuario_encontrado)
    else:
        print("Inserção inválida")

        
    
#|------------------------ atualização no usuario e JSON -----------------------------|
def atualizar_dados():
    """
    - Lê e carrega os dados do arquivo JSON.

    Parâmetro:
    - Nenhum

    Retorne:
    - Lista com os dados carregados do arquivo.
    """
    with open(caminho, 'r', encoding='utf-8') as file:
        return json.load(file)


def salvar_dados(banco_dados):
    """
    - Salva os dados atualizados no arquivo JSON.

    Parâmetro:
    - banco_dados: lista com os dados a serem salvos.

    Retorne:
    - Nenhum
    """
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco_dados, f, indent=4, ensure_ascii=False)


def atualizar_usuario(usuario_encontrado, campo, dados_novos):
    """
    - Atualiza um campo específico de um usuário e salva os dados atualizados.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do usuário logado.
    - campo: string representando o campo a ser atualizado.
    - dados_novos: novo valor a ser atribuído ao campo.

    Retorne:
    - Lista com os dados atualizados.
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

#|-----------------------------------------------------------------------------------|

#|------------------------ atualização de dados -------------------------------------|
def atualizar_nome(usuario_encontrado):
    """
    - Atualiza o nome do restaurante após validação.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    while True:
        dados_novos = input("Atualize seu nome (Digite 2 para voltar): ")
        if validador_nome(dados_novos):
            break
        elif dados_novos == '2':
            print("Voltando para a edição de perfil. . .")
            editar_perfil(usuario_encontrado)
    
    print("Descrição adicionada com sucesso!")
    atualizar_usuario(usuario_encontrado, 'nome', dados_novos)
    print("Nome do restaurante atualizado com sucesso!")
    mostrar_perfil(usuario_encontrado)


def atualizar_senha(usuario_encontrado):
    """
    - Atualiza a senha do restaurante após verificação da identidade.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    atualizando = True
    while atualizando:
        print('Confirme que é você. (Digite 2 para voltar.)')
        email = input("Digite seu email: ")
        if email != '2':
            senha = pwinput.pwinput(prompt='Digite sua senha: ', mask='*')
            if usuario_encontrado.get('email') == email and usuario_encontrado.get('senha') == criptografador(senha):
                while True:
                    dados_novos = pwinput.pwinput(prompt="Atualize sua senha (Digite 2 para voltar): ", mask='*')
                    if dados_novos != '2':
                        confirmacao = pwinput.pwinput(prompt="Digite sua senha novamente: ", mask='*')
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


def adicionar_cidade(usuario_encontrado):
    """
    - Adiciona ou atualiza a cidade no perfil do restaurante.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    if 'cidade' not in usuario_encontrado:
        usuario_encontrado['cidade'] = ""
    
    dados_novos = input("Digite a cidade onde seu restaurante reside: ")
    atualizar_usuario(usuario_encontrado, 'cidade', dados_novos)
    
    print("Cidade adicionada com sucesso!")
    mostrar_perfil(usuario_encontrado)


def adicionar_palavraChave(usuario_encontrado):
    """
    - Adiciona ou atualiza as palavras-chave do restaurante.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    if 'palavra-chave' not in usuario_encontrado:
        usuario_encontrado['palavra-chave'] = ""
    
    dados_novos = input("Digite a(s) palavra(s)-chave a ser(em) adicionada(s): ")
    atualizar_usuario(usuario_encontrado, 'palavra-chave', dados_novos)
    
    print("Palavras-chaves adicionadas com sucesso!")
    mostrar_perfil(usuario_encontrado)


def adicionar_descricao(usuario_encontrado):
    """
    - Adiciona ou atualiza a descrição do restaurante.

    Parâmetro:
    - usuario_encontrado: dicionário com os dados do restaurante logado.
    """
    if 'descricao' not in usuario_encontrado:
        usuario_encontrado['descricao'] = ""
    
    dados_novos = input("Digite a cidade onde seu restaurante reside: ")
    atualizar_usuario(usuario_encontrado, 'descricao', dados_novos)
    
    print("Descrição adicionada com sucesso!")
    mostrar_perfil(usuario_encontrado)


    
    
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
        atualizar_nome(usuario_encontrado)
    elif opc == 2:
        atualizar_senha(usuario_encontrado)
    elif opc == 3:
        adicionar_cidade(usuario_encontrado)
    elif opc == 4:
        adicionar_palavraChave(usuario_encontrado)
    elif opc == 5:
        adicionar_descricao(usuario_encontrado)
    elif opc == 6:
        apagar_conta(usuario_encontrado)
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
