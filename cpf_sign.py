end = False
caracteres = 0

while end == False:

    
    if caracteres == 0:
        cpf = str(input('Insira seu CPF (Utilize . e -):'))
    else:
        cpf = str(input('Tente novamente:'))
    
    caracteres = 0
    end = True

    for digito in cpf:
        caracteres += 1
        if end == True:
            if digito in ["1","2","3","4","5","6","7","8","9","0", "-","."]:
                end = True
            else:
                end = False

    if end == False:
        print('Erro. Apenas são permitidos números e símbolos: - .')

    if end == True:
        if caracteres == 14 or caracteres == 11:
            end = True
        else:
            print('Erro. Número de caractéres está incorreto.')
            end = False

    if "." in cpf or "-" in cpf:
        if end == True:
            if "." in cpf:
                if cpf.count('.') == 2:
                    if cpf[3] != '.' or cpf[7] != '.':
                        print('Erro. Ponto final em posição inválida.')
                    else:
                        end = True
                else:
                    print('Insira os pontos finais em suas determinadas posições.')
                    end = False
            else:
                print('Insira os pontos finais em suas determinadas posições.')
                end = False
            
        if end == True:    
            if "-" in cpf:
                if cpf.count("-") == 1:
                    if cpf[11] != '-':
                        print('Erro. Travessão em posição inválida.')
                    else:
                        print('Seu CPF foi cadastrado com sucesso.')
                        end = True
                else:
                    print('Erro. Travessão em posição inválida.')
                    end = False
            else:
                print('Insira um travessão antes dos dois últimos dígitos.')
                end = False
      
    elif end == True:
        if caracteres == 11:
            print('Seu CPF foi cadastrado com sucesso.')
            end = True