import os
import json


class CardapioRestaurante:
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


def add_prato(usuario_encontrado):
    nome_restaurante = usuario_encontrado.get('nome')

    print("------------- Adicionar Prato -------------")
    nome_prato = input("Digite o nome do prato: ")
    descricao_prato = input("Digite a descrição do prato: ")
    palavras_chave = input("Digite as palavras-chaves: ")
    preco = float(input("Digite o preço (caso seja um número inteiro, coloque .0 no final): "))

    prato_novo = CardapioRestaurante(nome_prato, descricao_prato, preco, palavras_chave)

    caminho_json = 'cardapio.json'

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
    
    print("\nPrato adicionado com sucesso!")
    cardapio(usuario_encontrado)



def cardapio(usuario_encontrado):
    nome_restaurante = usuario_encontrado.get('nome')
        
    print(f"Bem vindo a criação de cardápio, {nome_restaurante}!")
    print("Digite para qual aba deseja acessar: ")
    print("\n1. Adicionar prato \n2. Olhar cardapio")
    tecla = int(input("> "))
    
    if tecla == 1:
        add_prato(usuario_encontrado)
             
    elif tecla == 2:
        print("Em desenvolvimento . . .")
        
