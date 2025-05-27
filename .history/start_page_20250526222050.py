from login import *
from cliente_create import *
from menu_cliente import *

def main():
    def opcoes_cad_login(exe, usuario,repositorio_json, modulo):
        while exe:
            operacao = str(input('----------------------------\n  Selecione uma das seguintes opções:\n1. Login \n2. Cadastro\n0. Encerrar\n'))
            if operacao == '1': #Checa qual tecla foi pressionada e para onde o código deve seguir
                print(f'----------------------------\n  Realizando login de {usuario}...')
                login(repositorio_json)
                menu()
            elif operacao == '2':
                print(f'----------------------------\n  Realizando cadastro de {usuario}...')
                modulo()
            elif operacao == '0':
                print('----------------------------\n  Saindo...')
                exe = False
            else:
                print('----------------------------\n  Erro: Inserção inválida.')
 
    print('================================================================\n                     Bem vindo ao AllerGenie\n================================================================')
    
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
            print('Entrando como cliente...')
            cliente = True
            execucao = False
        elif opcao == '2':
            print('Entrando como empresa...')
            empresa = True
            execucao = False
        else:
            print('----------------------------\n  Erro: Inserção inválida.')

    execucao = True
    if empresa:
        opcoes_cad_login(execucao,'restaurantes','restaurantes.json',res_create)
    if cliente:
        opcoes_cad_login(execucao, 'clientes','clientes.json',cliente_create)
        

if __name__ == "__main__": #Define o seguimento como principal
    main()