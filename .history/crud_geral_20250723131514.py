import json
import pwinput
from validacoes import criptografador
from validacoes import *
from util import *




dados = []

class CRUD:
    
    """
    Representa um usuario do aplicativo AllerGenie.

    Atributos:
    nome (str): Nome do cliente
    | email (str): Email do cliente
    | senha (str): Senha do cliente
    
    """
    @staticmethod
    def atualizar_dados(caminho):
        with open(caminho, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    @staticmethod
    def salvar_dados(caminho, banco_dados):
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(banco_dados, f, indent=4, ensure_ascii=False)

    @staticmethod
    def atualizar_usuario(caminho, usuario_encontrado, campo, dados_novos):
        """
        - Atualiza um campo específico de um usuário e salva os dados atualizados.

        Parâmetro:
        - usuario_encontrado: dicionário com os dados do usuário logado.
        - campo: string representando o campo a ser atualizado.
        - dados_novos: novo valor a ser atribuído ao campo.

        Retorne:
        - Lista com os dados atualizados.
        """
        banco_dados = CRUD.atualizar_dados(caminho)
        id_usuario = usuario_encontrado.get('id')
        
        for usuario in banco_dados:
            if usuario.get('id') == id_usuario:
                usuario[campo] = dados_novos
                usuario_encontrado[campo] = dados_novos
        CRUD.salvar_dados(caminho, banco_dados)
    
    def apagar_conta(self, usuario_encontrado):
        
        id_usuario = usuario_encontrado.get('id_usuario')

        exc = True
        print("Deseja continuar? ")
        print("\n1. Sim \n2. Não")
        opc = int(input("> "))
        
        if opc == 1:
            email = input("Digite seu Email: ")
            senha = input("Digite sua Senha: ")
        
            while exc:
                banco_dados = CRUD.atualizar_dados()
                if usuario_encontrado.get('email') == email and usuario_encontrado.get('senha') == senha:
                    confir = input("Escreva 'Confirmo' para confirmar a exclusão da sua conta: ")
            
                    if confir == 'Confirmo':
                        for u in banco_dados:
                            if u.get('id_usuario') == id_usuario:
                                banco_dados.remove(u)
                                break
                        
                        CRUD.salvar_dados(banco_dados)
                        exc = False
                else:
                    print("Tente novamente")
                    exc = True
        elif opc == 2:
            print("Voltando para o perfil. . .")
            return
        else: 
            print("Inválido")
            CRUD.editar_perfil(usuario_encontrado)


        return banco_dados
    
    @staticmethod
    def atualizar_nome(caminho, usuario_encontrado):
        """
        - Atualiza o nome do restaurante após validação.

        Parâmetro:
        - usuario_encontrado: dicionário com os dados do restaurante logado.
        """
        dados_novos = input("Atualize seu nome: ")
        CRUD.atualizar_usuario(caminho, usuario_encontrado, 'nome', dados_novos)
        print(Utils.pinta("--- Nome atualizado com sucesso!", 'verde_claro'))
        return

    @staticmethod
    def atualizar_email(caminho, usuario_encontrado):
        dados_novos = input("Atualize seu email: ")
        CRUD.atualizar_usuario(caminho, usuario_encontrado, 'email', dados_novos)
        print(Utils.pinta("--- Email atualizado com sucesso!", 'verde_claro'))
        return
    
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
                                CRUD.atualizar_usuario(usuario_encontrado, 'senha', criptografador(dados_novos))
                                print(Utils.pinta("--- Senha modificada com sucesso!", 'verde_claro'))
                                return
                        elif dados_novos == '2':
                            print("Voltando para a edição de perfil. . .")
                            return
                else:
                    print("Login inválido. Insira dados novamente ou retorne a edição de perfil inserindo '0'.")
            elif email == '2':
                print("Voltando para a edição de perfil. . .")
                return
            else:
                print('Inserção inválida')

    @staticmethod
    def adicionar_cidade(caminho, usuario_encontrado):
        """
        - Adiciona ou atualiza a cidade no perfil do restaurante.

        Parâmetro:
        - usuario_encontrado: dicionário com os dados do restaurante logado.
        """
        
        if 'cidade' not in usuario_encontrado:
            usuario_encontrado['cidade'] = ""
        
        dados_novos = input("Digite sua cidade: ")
        usuario_encontrado['cidade'] = dados_novos
        banco_dados = CRUD.atualizar_dados(caminho)

        id_usuario = usuario_encontrado.get('id')
        for usuario in banco_dados:
            if usuario.get('id') == id_usuario:
                usuario['cidade'] = dados_novos
                break 
        
        print(Utils.pinta("--- Cidade atualizada com sucesso!", 'verde_claro'))
        CRUD.salvar_dados(caminho, banco_dados)
        return

    def __init__(self, nome_usuario, email, senha_1): #Adiciona atributos às instâncias
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = senha_1

    def criador_dic(self): #Converte todas as intâncias em dicionarios
        return {
            "nome": self.nome_usuario,
            "email": self.email,
            "senha": criptografador(self.senha), #Criptografa a senha inserida
            "id": str(id(self.email))
        }
    
        
    

        
class CrudRestaurante(CRUD):
    def __init__(self, nome_usuario=None, email=None, senha_1=None, cnpj=None, descricao=None, palavras_chave=None, avaliacao=None):
        super().__init__(nome_usuario, email, senha_1)
        self.cnpj = cnpj
        self.descricao = descricao
        self.palavras_chave = palavras_chave
        self.avaliacao = avaliacao if avaliacao is not None else {
            'media': 0.0,
            'soma_avaliacoes': 0,
            'quantidade_avaliacoes': 0
        }
        
        
    def adicionar_palavraChave(usuario_encontrado):
        """
        - Adiciona ou atualiza as palavras-chave do restaurante.

        Parâmetro:
        - usuario_encontrado: dicionário com os dados do restaurante logado.
        """
        if 'palavra-chave' not in usuario_encontrado:
            usuario_encontrado['palavra-chave'] = ""

        dados_novos = input("Digite a(s) palavra(s)-chave a ser(em) adicionada(s): ")
        CRUD.atualizar_usuario('bancos_json/restaurantes.json', usuario_encontrado, 'palavra-chave', dados_novos)

        Utils.limpar_tela()
        print(Utils.pinta("--- Palavras-chave modificada com sucesso!", 'verde_claro'))
        return
    
    def adicionar_descricao(usuario_encontrado):
        """
        - Adiciona ou atualiza a descrição do restaurante.

        Parâmetro:
        - usuario_encontrado: dicionário com os dados do restaurante logado.
        """
        if 'descricao' not in usuario_encontrado:
            usuario_encontrado['descricao'] = ""
        
        dados_novos = input("Digite a descrição do seu restaurante: ")
        CRUD.atualizar_usuario('bancos_json/restaurantes.json', usuario_encontrado, 'descricao', dados_novos)
        
        Utils.limpar_tela()
        print(Utils.pinta("--- Descrição adicionada com sucesso!", 'verde_claro'))
        return

    def criador_dic(self):
        dados = super().criador_dic()
        if self.cnpj:
            dados["cnpj"] = self.cnpj
        if self.descricao:
            dados["descricao"] = self.descricao
        if self.palavras_chave:
            dados["palavra-chave"] = self.palavras_chave
            
        dados["avaliacao"] = self.avaliacao
        return dados


class CrudCliente(CRUD):
    
    @staticmethod
    def adicionar_alergia(caminho, usuario_encontrado):
        id_usuario = usuario_encontrado.get('id')
        
        if 'alergia' not in usuario_encontrado:
            usuario_encontrado['alergia'] = ""
        
        dados_novos = input("Digite sua(s) alergia(s): ")
        usuario_encontrado['alergia'] = dados_novos
        
        banco_dados = CRUD.atualizar_dados(caminho)
        
        for usuario in banco_dados:
            if usuario.get('id') == id_usuario:
                usuario['alergia'] = dados_novos
                break
            
        Utils.limpar_tela()
        print(Utils.pinta("--- Alergia(s) adicionada(s) com sucesso!", 'verde_claro'))
        CRUD.salvar_dados(caminho, banco_dados)
        return
        