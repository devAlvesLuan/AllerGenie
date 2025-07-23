from crud_geral import CRUD

caminho_menu = 'bancos_json/menu_pesssoal.json'
caminho_restaurantes = 'bancos_json/restaurantes.json'

class Biblioteca:
    
    def visualizar_menus(usuario_encontrado):
        dados_menus = CRUD.ler_dados('bancos_json/menu_pessoal.json')
        chave_usuario = usuario_encontrado['id']

        if chave_usuario not in dados_menus:
            print("Você ainda não criou menus personalizados.")
            return

        print(f"\nSeus menus:")
        for nome_menu, restaurantes in dados_menus[chave_usuario].items():
            print(f"\nMenu: {nome_menu} ({len(restaurantes)} restaurantes)")
            i = 0
            for restaurante in restaurantes:
                i += 1
                print("------------------------------------------------")
                print(f"{i}.\nRestaurante: ", restaurante.get('nome'))
                print("Email: ", restaurante.get('email'))
                print("CNPJ: ", restaurante.get('cnpj'))
                print("Cidade: ", restaurante.get('cidade', 'Não inserido.'))
                print("Palavras-Chaves: ", restaurante.get('palavra-chave', 'Não inserido.'))
                print("Descrição: ", restaurante.get('descricao', 'Não inserido.'))
                print("Avaliação:", restaurante.get('avaliacao', {}).get('media', 'Sem avaliação'))
                print("-------------------------------------------------")
                

    def criar_menu(nome_menu, usuario_encontrado):
        dados_menus = CRUD.ler_dados('bancos_json/menu_pessoal.json')
        chave_usuario = usuario_encontrado['id']
        
        if chave_usuario not in dados_menus:
            dados_menus[chave_usuario] = {}

        if nome_menu in dados_menus[chave_usuario]:
            print("Você já possui um menu com esse nome.")
            return

        dados_menus[chave_usuario][nome_menu] = []
        CRUD.salvar_dados('bancos_json/menu_pessoal.json', dados_menus)
        print(f"Menu '{nome_menu}' criado com sucesso!")

    def adicionar_restaurante(nome_menu, caminho, usuario_encontrado):
        dados_menus = CRUD.ler_dados('bancos_json/menu_pessoal.json')
        chave_usuario = usuario_encontrado['id']

        if chave_usuario not in dados_menus or nome_menu not in dados_menus[chave_usuario]:
            print("Menu não encontrado.")
            return

        print(f"Digite o nome (ou parte do nome) do restaurante que deseja adicionar ao menu '{nome_menu}':")
        nome_busca = input("> ").lower()

        restaurantes_disponiveis = CRUD.ler_dados(caminho)
        restaurante_encontrado = None

        for restaurante in restaurantes_disponiveis:
            if nome_busca in restaurante.get('nome', '').lower():
                restaurante_encontrado = restaurante
                break

        if not restaurante_encontrado:
            print("Restaurante não encontrado.")
            return

        if restaurante_encontrado in dados_menus[chave_usuario][nome_menu]:
            print("Este restaurante já está neste menu.")
            return

        dados_menus[chave_usuario][nome_menu].append(restaurante_encontrado)
        CRUD.salvar_dados('bancos_json/menu_pessoal.json', dados_menus)
        print("Restaurante adicionado ao menu com sucesso!")
            

    def visualizar_favoritos(usuario_encontrado):
        dados_favoritos = CRUD.ler_dados('bancos_json/favoritos.json')

        chave_usuario = usuario_encontrado['id']

        if chave_usuario not in dados_favoritos:
            print("Você ainda não tem restaurantes favoritos.")
            return
        else:
            print(f"\nSeus restaurantes favoritos:")
            i = 0
            for restaurante in dados_favoritos[chave_usuario]:
                i += 1
                print("------------------------------------------------")
                print(f"{i}.\nRestaurante: ", restaurante.get('nome'))
                print("Email: ", restaurante.get('email'))
                print("CNPJ: ", restaurante.get('cnpj'))
                print("Cidade: ", restaurante.get('cidade', 'Não inserido.'))
                print("Palavras-Chaves: ", restaurante.get('palavra-chave', 'Não inserido.'))
                print("Descrição: ", restaurante.get('descricao', 'Não inserido.'))
                print("Avaliação:", restaurante.get('avaliacao', {}).get('media', 'Sem avaliação'))
                print("-------------------------------------------------")
                
    def favoritar(caminho_restaurantes, usuario_encontrado):
        print('Qual restaurante gostaria de favoritar?')
        opc = str(input("> "))
        dados_favoritos = CRUD.ler_dados('bancos_json/favoritos.json')

        chave_usuario = usuario_encontrado['id']
        
        if chave_usuario not in dados_favoritos:
            dados_favoritos[chave_usuario] = []
        encontrado = False
        for restaurante in caminho_restaurantes:
            if opc.lower() in restaurante.get('nome', '').lower():
                encontrado = True
                if restaurante not in dados_favoritos[chave_usuario]: 
                    dados_favoritos[chave_usuario].append(restaurante)
                    CRUD.salvar_dados('bancos_json/favoritos.json', dados_favoritos)
                    print('Favorito salvo com sucesso!')
                    break
                else:
                    print('Favorito já anteriormente cadastrado.')
                    break
        if not encontrado:
            print('Restaurante não encontrado... Tente novamente.')

    def remover_favorito(usuario_encontrado):
        dados_favoritos = CRUD.ler_dados('bancos_json/favoritos.json')
        chave_usuario = usuario_encontrado['id']

        if chave_usuario not in dados_favoritos:
            print("Você não tem restaurantes favoritos para remover.")
            return

        print("Qual restaurante você deseja remover dos favoritos?")
        nome_remover = str(input("> ")).lower()
        restaurantes = dados_favoritos[chave_usuario]
        encontrado = False

        for restaurante in restaurantes:
            if nome_remover in restaurante.get('nome', '').lower():
                print(f'Tem certeza que quer remover {restaurante.get('nome')} da sua lista de favoritos?\n1. Sim\n2. Não')
                opc = str(input("> "))
                if opc == '1':
                    restaurantes.remove(restaurante)
                    CRUD.salvar_dados('bancos_json/favoritos.json', dados_favoritos)
                    print(f"Restaurante '{restaurante.get('nome')}' removido com sucesso.")
                    encontrado = True
                    break
                else:
                    break

        if not encontrado:
            print("Restaurante não encontrado nos seus favoritos.")

    def favoritos_opcoes(usuario_encontrado):
        Biblioteca.visualizar_favoritos(usuario_encontrado)
        print('1. Adicionar favoritos\n2. Remover favoritos\n3. Voltar')
        opc = str(input("> "))
        if opc == '1':
            Biblioteca.favoritar(CRUD.ler_dados(caminho_restaurantes), usuario_encontrado)
            Biblioteca.favoritos_opcoes(usuario_encontrado)
        if opc == '2':
            Biblioteca.remover_favorito(usuario_encontrado)
            Biblioteca.favoritos_opcoes(usuario_encontrado)
        elif opc == '3':
            Biblioteca.menu_pessoal(usuario_encontrado)
        else:
            print('Opção inválida. Tente novamente')
            Biblioteca.favoritos_opcoes(usuario_encontrado)
    
    def menu_interno(usuario_encontrado):
        dados_menus = CRUD.ler_dados('bancos_json/menu_pessoal.json')
        chave_usuario = usuario_encontrado['id']

        if chave_usuario not in dados_menus or not dados_menus[chave_usuario]:
            print("Você ainda não possui menus personalizados.")
            return

        Biblioteca.visualizar_menus(usuario_encontrado)
        while True:
            print("Digite o nome do menu que deseja editar:")
            nome_menu = input("> ")

            encontrado = False
            for restaurante in dados_menus[usuario_encontrado['id']]:
                if nome_menu.lower().split() in restaurante.lower().split():
                    encontrado = restaurante

            if encontrado:    
                while True:
                    print(f"\nMenu: {encontrado}")
                    print("1. Adicionar restaurante")
                    print("2. Remover restaurante")
                    print("3. Voltar")
                    opc = input("> ")

                    if opc == '1':
                        Biblioteca.adicionar_restaurante(encontrado, 'bancos_json/restaurantes.json', usuario_encontrado)
                    elif opc == '2':
                        Biblioteca.re(encontrado, usuario_encontrado)
                    elif opc == '3':
                        Biblioteca.menu_opcoes(usuario_encontrado)
                    else:
                        print("Opção inválida.")
            else:
                print('Menu não encontrado. Tente novamente. (Pressione 2 para voltar)')
                opc_saida = str(input("> "))
                if opc_saida == '2':
                    Biblioteca.menu_opcoes(usuario_encontrado)
                

    def menu_opcoes(usuario_encontrado):
        while True:
            print('Qual operação de MENU gostaria de realizar?')
            print('1. Criar MENU\n2. Editar MENU\n3. Voltar')
            opc = str(input("> "))
            if opc == '1':
                print('Insira o nome do MENU personalizado que gostaria de criar.')
                nome = str(input("> "))
                Biblioteca.criar_menu(nome, usuario_encontrado)
            if opc == '2':
                Biblioteca.menu_interno(usuario_encontrado)
            if opc == '3':
                Biblioteca.menu_pessoal(usuario_encontrado)

    def menu_pessoal(usuario_encontrado): 
        print(f'Bem-vindo(a) ao MENU Pessoal, {usuario_encontrado.get('nome')}. \nAqui suas opções de prato ou de restaurante são salvas de forma personalizada.')

        while True:
            print('1. Favoritos\n2. MENU Pessoal\n3. Voltar')
            opc = str(input("> "))
            if opc == '1':
                Biblioteca.favoritos_opcoes(usuario_encontrado)
            elif opc == '2':
                Biblioteca.menu_opcoes(usuario_encontrado)
            elif opc == '3':
                print('Voltando ao menu principal...')
                from menu_cliente import menu_client  # ← import local
                menu_client(usuario_encontrado)
                break
            else:
                print('Erro: Opção inválida. Tente novamente.')