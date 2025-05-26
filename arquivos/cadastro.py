


class Restaurante:
    def __init__(self, nome_restaurante, cnpj, email, senha):
        self.nome_restaurante = nome_restaurante
        self.cnpj = cnpj
        self.email = email
        self.senha = senha


def executar_cadastro():
    print("---- Seja bem-vindo a tela de cadastro! ----")
    print("-- Digite os seguinte dados: --")
    coletar_dados_cadastro()



def coletar_dados_cadastroRestaurante():
    nome_restaurante = input("Nome do restaurante: ")
    cnpj = input("CNPJ (somente números): ")
    email = input("Email: ")
    senha = input("Senha: ")

    # Aqui você pode adicionar validações antes de retornar, se quiser

    













