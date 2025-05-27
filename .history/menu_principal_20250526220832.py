import os
import json
banco_dados = []
id_usuario = None
caminho = 'clientes.json'
 

def apagar_conta(usuario_encontrado):
    id_usuario = usuario_encontrado.get('id')

    exc = True
    print("Deseja continuar? ")
    print("\n1. Sim \n2. Não")
    opc = int(input("> "))
    
    if opc == 1:
        email = input("Digite seu Email: ")
        senha = input("Digite sua Senha: ")
    
        while exc:
            banco_dados = atualizar_dados()
            if usuario_encontrado.get('email') == email and usuario_encontrado.get('senha') == senha:
                confir = input("Escreva 'Confirmo' para confirmar a exclusão da sua conta: ")
        
                if confir == 'Confirmo':
                    for u in banco_dados:
                        if u.get('id_uso') == id_usuario:
                            banco_dados.remove(u)
                            break
                    
                    salvar_dados(banco_dados)
                    exc = False
            else:
                print("Tente novamente")
                exc = True
    elif opc == 2:
        print("Voltando para o perfil. . .")
        mostrar_perfil(usuario_encontrado)
    else: 
        print("Inválido")
        editar_perfil(usuario_encontrado)
        
    
    

def atualizar_dados():
    with open(caminho, 'r', encoding='utf-8') as file:
        return json.load(file)

def salvar_dados(banco_dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco_dados, f, indent=4, ensure_ascii=False)

def atualizar_usuario(usuario_encontrado, campo, dados_novos):
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
    dados_novos = input("Atualize seu nome: ")
    
    atualizar_usuario(usuario_encontrado, 'nome', dados_novos)
    mostrar_perfil(usuario_encontrado)


def atualizar_email(usuario_encontrado):
    
    dados_novos  = input("Atualize seu senha: ")
    atualizar_usuario(usuario_encontrado, 'senha', dados_novos)
    mostrar_perfil(usuario_encontrado)
    
    
def adicionar_alergia(usuario_encontrado):
    
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
    
    if 'cidade' not in usuario_encontrado:
        usuario_encontrado['cidade'] = ""
    
    dados_novos = input("Digite sua cidade: ")
    usuario_encontrado['cidade'] = dados_novos
    banco_dados = atualizar_dados()
    
    for usuario in banco_dados:
        if usuario.get('id') == id_usuario:
            usuario['cidade'] = usuario_encontrado['cidade'] 
            
            break 
    
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
        atualizar_email(usuario_encontrado)
    elif opc == 3:
        adicionar_alergia(usuario_encontrado)
    elif opc == 4:
        adicionar_cidade(usuario_encontrado)
    elif opc == 5:
        apagar_conta(usuario_encontrado)
    elif opc == 6:
        print("Saindo . . .")
        menu(usuario_encontrado)
        return
    else:
        print("Opção inválida.")

    

def mostrar_perfil(usuario_encontrado):
    alergia = usuario_encontrado.get('alergia')
    
    execucao = True
    print("------ PERFIL ------")
    print("\nNome: ", usuario_encontrado.get('nome'))
    print("Email: ", usuario_encontrado.get('email'))
    print("Alergias: ", usuario_encontrado.get('alergia'))
    print("Cidade: ", usuario_encontrado.get('cidade'))
    
    
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
            menu(usuario_encontrado)
            execucao = False

def menu(usuario_encontrado):
    execucao = True
    while execucao:
        print(f"Bem vindo ao AllerGenie, {usuario_encontrado.get('nome')}!\n")
        print("Pressione o número referente a algum dessas abas: ")
        print("1. Perfil \n2. Pesquisa \n3. Biblioteca\n")
        tecla = int(input("> "))

        if tecla not in [1, 2, 3]:
            print("\nErro: Pressione um número válido\n")
            continue

        if tecla == 1:
            mostrar_perfil(usuario_encontrado)
            execucao = False  
            break
            

