import keyboard
from login import *
from res_create import *
from menu_principal import *

def main():
    print('================================================================\n                     Bem vindo ao AllerGenie\n================================================================')
    print('----------------------------\n  Pressione a \'Barra de Espaço\' para começar')
    keyboard.wait('space_bar') #Espera uma tecla até seguir em frente
    print('----------------------------\n  Iniciando...')


    print('----------------------------\n  Selecione uma das seguintes opções:\n1. Login \n2. Cadastro\nESCAPE. Encerrar')

    execucao = True
    while execucao:      #Mantém o código operando
        if keyboard.read_key() == '1': #Checa qual tecla foi pressionada e para onde o código deve seguir
            print('----------------------------\n  Realizando login da empresa...')
            login('restaurantes.json')
            menu()
        elif keyboard.read_key() == '2':
            print('----------------------------\n  Realizando cadastro da empresa...')
            res_create()
            menu()
        elif keyboard.read_key() == 'esc':
            print('----------------------------\n  Saindo...')
            execucao = False
        else:
            print('----------------------------\n  Erro: Inserção inválida.')
        

if __name__ == "__main__": #Define o seguimento como principal
    main()