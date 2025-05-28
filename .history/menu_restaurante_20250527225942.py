import json
banco_dados = []
caminho = 'restaurantes.json'
 

def apagar_conta(usuario_encontrado):
    
    id_usuario = usuario_encontrado.get('id_usuario')
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
                    for usuario in banco_dados:
                        if usuario.get('id_usuario') == id_usuario:
                            banco_dados.remove(usuario)
                            break
                    
                    salvar_dados(banco_dados)
                    exc = False
                    print("Conta ap")
            else:
                print("Tente novamente")
                exc = True
    elif opc == 2:
        print("Voltando para o perfil. . .")
        mostrar_perfil(usuario_encontrado)
    else: 
        print("Inválido")
        editar_perfil(usuario_encontrado)
        
    
#|------------------------ atualização no usuario e JSON -----------------------------|
def atualizar_dados():
    with open(caminho, 'r', encoding='utf-8') as file:
        return json.load(file)

def salvar_dados(banco_dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco_dados, f, indent=4, ensure_ascii=False)

def atualizar_usuario(usuario_encontrado, campo, dados_novos):
    banco_dados = atualizar_dados()
    id_usuario = usuario_encontrado.get('id_usuario')
    
    for usuario in banco_dados:
        if usuario.get('id_usuario') == id_usuario:
            usuario[campo] = dados_novos
            usuario_encontrado[campo] = dados_novos
            salvar_dados(banco_dados)
            break  

    return banco_dados
#|-----------------------------------------------------------------------------------|

#|------------------------ atualização de dados -------------------------------------|
def atualizar_nome(usuario_encontrado):
    dados_novos = input("Atualize o nome do restaurante: ")
    
    
    print("Descrição adicionada com sucesso!")
    atualizar_usuario(usuario_encontrado, 'nome', dados_novos)
    print("Nome do restaurante atualizado com sucesso!")
    mostrar_perfil(usuario_encontrado)
    

def atualizar_senha(usuario_encontrado):
    
    dados_novos  = input("Atualize seu senha: ")
    atualizar_usuario(usuario_encontrado, 'senha', dados_novos)
    print("Senha modificada com sucesso!")
    mostrar_perfil(usuario_encontrado)
    
   
    

def adicionar_cidade(usuario_encontrado):
    
    if 'cidade' not in usuario_encontrado:
        usuario_encontrado['cidade'] = ""
    
    dados_novos = input("Digite a cidade onde seu restaurante reside: ")
    atualizar_usuario(usuario_encontrado, 'cidade', dados_novos)
    
    print("Cidade adicionada com sucesso!")
    mostrar_perfil(usuario_encontrado)

def adicionar_palavraChave(usuario_encontrado):
    
    if 'palavra-chave' not in usuario_encontrado:
        usuario_encontrado['palavra-chave'] = ""
    
    dados_novos = input("Digite a cidade onde seu restaurante reside: ")
    atualizar_usuario(usuario_encontrado, 'palavra-chave', dados_novos)
    
    
    print("Palavras-chaves adicionadas com sucesso!")
    mostrar_perfil(usuario_encontrado)

def adicionar_descricao(usuario_encontrado):
    
    if 'descricao' not in usuario_encontrado:
        usuario_encontrado['descricao'] = ""
    
    dados_novos = input("Digite a adesc: ")
    atualizar_usuario(usuario_encontrado, 'descricao', dados_novos)
        
    print("Descrição adicionada com sucesso!")
    mostrar_perfil(usuario_encontrado)
  
    
    
def editar_perfil(usuario_encontrado):
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
        menu(usuario_encontrado)
        return
    else:
        print("Opção inválida.")




def mostrar_perfil(usuario_encontrado):
    alergia = usuario_encontrado.get('alergia')
    
    execucao = True
    print("------ PERFIL ------")
    print("\nRestaurante: ", usuario_encontrado.get('nome'))
    print("Email: ", usuario_encontrado.get('email'))
    print("CNP-J: ", usuario_encontrado.get('cnpj'))
    print("Cidade: ", usuario_encontrado.get('cidade', ''))
    print("Palavras-Chaves: ", usuario_encontrado.get('palavra-chave', ''))
    print("Descrição: ", usuario_encontrado.get('descricao', ''))
    
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
            menu(usuario_encontrado)
            execucao = False



def menu(usuario_encontrado):
    
    execucao = True
    while execucao:
        print(f"Bem vindo ao AllerGenie, {usuario_encontrado.get('nome')}!\n")
        print("Pressione o número referente a algum dessas abas: ")
        print("1. Perfil \n2. Cárdapio")
        tecla = int(input("> "))

        if tecla not in [1, 2]:
            print("\nErro: Pressione um número válido\n")
            continue

        if tecla == 1:
            mostrar_perfil(usuario_encontrado)
            execucao = False  
            break
        elif tecla == 2:
            print("")
            #cardapio()
            

