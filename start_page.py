execucao = True
import keyboard


print('Bem vindo ao AllerGenie!\nSelecione uma das seguintes opções:\n1. Login \n2. Cadastro')

while execucao == True:
    if keyboard.read_key() == '1':
        print('Realizando login')
        execucao = False
    elif keyboard.read_key() == '2':
        print('Realizando cadastro')
        execucao = False
    else:
        print('Inserção inválida.')
    
#__name__ == '__main__'