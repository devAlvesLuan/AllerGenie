from cliente_create import *
from res_create import res_create
import shutil
import os
from menu_cliente import *
from menu_restaurante import *
from util import *

if os.path.exists("pycache"):
    shutil.rmtree("pycache")
if os.path.exists(".history"):
    shutil.rmtree(".history")

def main():
    """
     - Função principal do aplicativo    
      
    """
    
    
    def opcoes_cad_login(exe, usuario,repositorio_json, modulo_cadastro):
        
        """
        - Realiza qual segmento o usuário deseja (cadastro, login)
        
        Parâmetros: 
        exe (bool): Serve como moderador do While
        usuario (str): O tipo de usuário (cliente, restaurante/empresa)
        repositorio_json (json): Dependendo do usuario, será o repositório JSON que aliementará
        modulo_cadastro: Modulo de funcionalidade para criação de conta
        
        """
        
        
        
        while exe:
            operacao = str(input('----------------------------\n  Selecione uma das seguintes opções:\n1. Login \n2. Cadastro\n0. Encerrar\n'))
            if operacao == '1': #Checa qual tecla foi pressionada e para onde o código deve seguir
                Utils.limpar_tela()
                print(f'---------------------------------------\n  Realizando login de {usuario}...')
                from login import login
                login(repositorio_json)
            elif operacao == '2':
                Utils.limpar_tela()
                print(f'---------------------------------------\n  Realizando cadastro de {usuario}...')
                modulo_cadastro()
                from login import login
                login(repositorio_json)

            elif operacao == '0':
                print(Utils.pinta('Saindo . . .', 'amarelo'))
                exe = False
            else:
                print('----------------------------\n  Erro: Inserção inválida.')
    
    Utils.limpar_tela()
    print(Utils.pinta('================================================================\n                     Bem vindo ao AllerGenie\n================================================================', 'verde'))
    
    execucao = True
    while execucao:
        comeco = input('----------------------------\n  Pressione \'Enter\' para começar')
        if comeco == '':
            print('----------------------------\n  Iniciando...')
            execucao = False

    execucao = True
    empresa = False
    cliente = False

    while execucao:
        opcao = str(input('----------------------------\n Gostaria de entrar como: \n1. Cliente\n2. Empresa\n').strip())
        if opcao == '1':
            Utils.limpar_tela()
            
            print('Entrando como cliente...')
            cliente = True
            execucao = False
        elif opcao == '2':
            Utils.limpar_tela()
            print('Entrando como empresa...')
            empresa = True
            execucao = False
        else:
            print('----------------------------\n  Erro: Inserção inválida.')

    execucao = True
    if empresa:
        opcoes_cad_login(execucao, 'restaurantes', 'bancos_json/restaurantes.json', res_create)
    if cliente:
        opcoes_cad_login(execucao, 'clientes', 'bancos_json/clientes.json', cliente_create)

if __name__ == "__main__": #Define o seguimento como principal
    main()