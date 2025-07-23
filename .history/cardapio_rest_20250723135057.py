import os
import json
from util import *

def ler_dados_json():
        """
        - Lê os dados dos arquivos JSON contendo informações dos restaurantes e cardápios.
        
        Retorne:
        - Uma tupla contendo dois elementos: (dados_restaurante, dados_cardapio)
        """
        caminho_cardapio = 'bancos_json/cardapio.json'
        
        with open(caminho_cardapio, 'r', encoding='utf-8') as file:
            dados_cardapio = json.load(file)
            
        return dados_cardapio

class CardapioRestaurante:
    
    """
    Representa um cliente do aplicativo AllerGenie.

    Atributos:
    prato (str): Nome do prato
    | descricao (str): O que tem no prato
    | preco (float): Preço do prato
    | palavra_chave (float): Palavras-chave do prato
    
    """
    
    
    def __init__(self, prato, descricao, preco, palavra_chave): #Adiciona atributos às instâncias
        self.prato = prato
        self.descricao = descricao
        self.palavras_chave = palavra_chave
        self.preco = preco

    def criador_dic_cardapio(self): #Converte todas as intâncias em dicionarios
        return {
            "nome-prato": self.prato,
            "descricao": self.descricao,
            "palavras-chave": self.palavras_chave,
            "preco": self.preco
        }

def funcao_menu(usuario_encontrado):
    from menu_restaurante import menu_empresa
    menu_empresa(usuario_encontrado)

def add_prato(usuario_encontrado):
    
    """
    - Adiciona um novo prato ao cardápio de um restaurante
    
    """
    
    nome_restaurante = usuario_encontrado.get('nome')

    print(Utils.pinta("------------- Adicionar Prato -------------", 'verde_claro'))
    nome_prato = input("Digite o nome do prato: ")
    descricao_prato = input("Digite a descrição do prato: ")
    palavras_chave = input("Digite as palavras-chaves: ")
    preco = float(input("Digite o preço (caso seja um número inteiro, coloque .0 no final): "))

    prato_novo = CardapioRestaurante(nome_prato, descricao_prato, preco, palavras_chave)

    caminho_json = 'bancos_json/cardapio.json'

    if os.path.exists(caminho_json):
        with open(caminho_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    else:
        dados = {}

    if nome_restaurante not in dados:
        dados[nome_restaurante] = []

    dados[nome_restaurante].append(prato_novo.criador_dic_cardapio())

    with open(caminho_json, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    
    print(Utils.pinta("--- Prato adicionado com sucesso!", 'verde_claro'))
    print("\nPrato adicionado com sucesso!")
    cardapio(usuario_encontrado)
    
def visualizar_cardapio(nome_restaurante):
    
    dados_cardapio = ler_dados_json()
    
    for nome_restaurante, pratos in dados_cardapio.items():
            print(f"\nCardápio do restaurante: {nome_restaurante}")
            for prato in pratos:
                nome_prato = prato.get('nome-prato')
                descricao = prato.get('descricao', 'Não encontrado')
                preco = prato.get('preco', 'Não encontrado')

                print("----------------------------------------------------------")
                print(f"||> Prato: {nome_prato}")
                print(f"||> Descrição: {descricao}")
                print(f"||> Preço: {preco}R$")
                print("----------------------------------------------------------")


def cardapio(usuario_encontrado):
    """
    - Exibe o menu de opções relacionado ao cardápio do restaurante logado.
    - Permite ao usuário adicionar pratos, visualizar o cardápio (em desenvolvimento) ou sair para o menu principal.

    Parâmetro:
    - usuario_encontrado (dict): dicionário contendo os dados do restaurante logado.

    """
    nome_restaurante = usuario_encontrado.get('nome')

    print(Utils.pinta("------ CARDÁPIO ------", 'amarelo'))
    print(f"Bem vindo à criação de cardápio, {nome_restaurante}!")
    print("Digite para qual aba deseja acessar: ")
    print("\n1. Adicionar prato \n2. Visualizar cardápio\n3. Sair")
    tecla = int(input("> "))
    
    while True:
        if tecla == 1:
            add_prato(usuario_encontrado)
        elif tecla == 2:
            visualizar_cardapio(nome_restaurante)
        elif tecla == 3:
            Utils.limpar_tela()
            print(Utils.pinta('Saindo . . .', 'amarelo'))
            funcao_menu(usuario_encontrado)
        else:
            print("Inserção inválida.")
