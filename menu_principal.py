import keyboard


def menu():
    print('================================================================\n                     Menu Principal\n================================================================')
    print('----------------------------\n  Selecione uma das seguintes opções:\n1. Pesquisar restaurantes e cardápios\n2. Perfil\nESCAPE. Encerrar')

    while execucao:      #Mantém o código operando
        if keyboard.read_key() == '1': #Checa qual tecla foi pressionada e para onde o código deve seguir
            print('----------------------------\n  Pesquisa...')
            execucao = False
        elif keyboard.read_key() == '2':
            print('----------------------------\n  Perfil...')
            execucao = False
        elif keyboard.read_key() == 'esc':
            print('----------------------------\n  Saindo...')
            execucao = False
        else:
            print('----------------------------\n  Erro: Inserção inválida.')