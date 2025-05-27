import keyboard
import json
dados = []

with open('clientes.json', 'w', encoding='utf-8') as f:
    dados = json.load()

def editar_perfil():
    
    print("------ EDIÇÃO DE PERFIL ------")
    
    print("Deseja modificar qual informação: ")
    print("\n1. Nome \n2. Email \n3. Alergias \n4. Cidade")
    opc = int(input(""))
    
    if opc == 1:
        nome = str(input("Digite seu nome: "))
        menu_principal()
        return nome




def mostrar_perfil():
    execucao = True
    print("------ PERFIL ------")
    print("\nNome: ")
    print("Email: ")
    print("Alergias: ")
    print("Cidade: ")
    
    
    while execucao:
        print("\n1. Editar Perfil \n2. Sair")
        opc = int(input(""))
        
        if opc not in [1,2]:
            print("Erro: opção inválida.")
            
        if opc == 1:
            print("REALIZANDO EDIÇÃO")
            editar_perfil()
            execucao = False
        elif opc == 2:
            print("SAINDO. . .")
            menu_principal()
            execucao = False
            

def menu_principal():
    execucao = True
    while execucao:
        print(f"Bem vindo ao AllerGenie, {nome}!\n")
        print("Pressione o número referente a algum dessas abas: ")
        tecla = int(input("1. Perfil \n2. Pesquisa \n3. Biblioteca\n"))

        if tecla not in [1, 2, 3]:
            print("\nErro: Pressione um número válido\n")
            continue

        if tecla == 1:
            mostrar_perfil()
            execucao = False  
            break
            
        
menu_principal()
    
    
    
    
    

    




        
    

