#Bibliotecas
import keyboard
from arquivos.res_create import *
from cliente_create import *

def main():
    print('================================================================\n                     Bem vindo ao AllerGenie\n================================================================')
    print('----------------------------\n  Pressione a \'Barra de Espaço\' para começar')
    keyboard.wait('space_bar') #Espera uma tecla até seguir em frente
    print('----------------------------\n  Iniciando...')

#Variáveis
execucao_um = True
execucao_dois = True
empresa = 'Empresa'
cliente = 'Cliente'



#Definir se é empresa ou cliente
while execucao_um == True:
    print('Bem vindo ao AllerGenie!\nSelecione uma das seguintes opções:\n1. Empresa \n2. Cliente ')
    
    tecla = keyboard.read_key() #Guarda a tecla pressionada

    #Erro de inserção inválida
    if tecla not in ['1', '2']:
        print("\nErro: Inserção inválida\n")
    else:
        execucao_um = False
    
    #Printa o que foi escolhido inicialmente
    if tecla == '1':
        print("\nEscolhido: ", empresa)
    elif tecla == '2':
        print("\nEscolhido: ", cliente)



#Escolher entre login e cadastro ou cancelar
while execucao_dois == True:
    tecla_log_cad = int(input('Bem vindo ao AllerGenie!\nSelecione uma das seguintes opções:\n1. Login \n2. Cadastro \n3. Cancelar : ', ))

    #Caso escolheu login
    if tecla_log_cad == 1:
        print('Realizando login')
        #Se a primeira escolha foi empresa
        if tecla == '1':
            print("Realizando o login de empresa")
        #Se a primeira escolha foi cliente
        elif tecla == '2':
            print("Realizando o login de cliente")

        execucao_dois = False

    
    #Caso escolheu cadastro
    elif tecla_log_cad == 2:
        print('Realizando cadastro')
        #Se a primeira escolha foi empresa
        if tecla == '1':
            print("Realizando o cadastro de empresa")
            res_create()
        #Se a primeira escolha foi cliente
        elif tecla == '2':
            print("Realizando o cadastro de cliente")
            client_create()

        execucao_dois = False
    elif tecla_log_cad == 3:
        print("Cancelando. . .")
        execucao_dois = False
    #Erro
    else:
        print('\nErro: Inserção inválida. Tente novamente\n')


#__name__ == '__main__'

