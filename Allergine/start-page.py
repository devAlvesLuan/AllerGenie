import login
import cadastro

print("---- Seja bem-vindo ao Allergine!! ----\n")
print("Escreva qual ação deseja:")
print("1 - Login\n2 - Cadastro")
acao = int(input("Número: "))


match acao:
    case 1:
        login.executar()
    case 2: 
        cadastro.executar_cadastro()

