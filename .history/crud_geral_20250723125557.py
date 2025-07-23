import json
from validacoes import criptografador


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
        banco_dados = CRUD.atualizar_dados(caminho)
        id_usuario = usuario_encontrado.get('id')
        
        for usuario in banco_dados:
            if usuario.get('id') == id_usuario:
                usuario[campo] = dados_novos
                usuario_encontrado[campo] = dados_novos
        CRUD.salvar_dados(caminho, banco_dados)
    
    @staticmethod
    def atualizar_nome(caminho, usuario_encontrado):
        dados_novos = input("Atualize seu nome: ")
        CRUD.atualizar_usuario(caminho, usuario_encontrado, 'nome', dados_novos)
        return

    @staticmethod
    def atualizar_email(caminho, usuario_encontrado):
        dados_novos = input("Atualize seu email: ")
        CRUD.atualizar_usuario(caminho, usuario_encontrado, 'email', dados_novos)
        return

    @staticmethod
    def adicionar_cidade(caminho, usuario_encontrado):
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
        
        CRUD.salvar_dados(caminho, banco_dados)
        return
        