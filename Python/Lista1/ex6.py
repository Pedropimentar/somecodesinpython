while True:

    nomeUsu = input("Digite seu nome de usuario ->")

    if len(nomeUsu) >= 8 and "#" not in nomeUsu and "!" not in nomeUsu:
        
        print(f"Usuario: {nomeUsu}")

        while True:

            senha = input("Digite sua senha ->")

            if( "#" in senha or "!" in senha): #verificacao de caractere especial
                
                if(len(senha) >= 8): #verificacao de tamanho, dessa forma a senha pode conter apenas um dos caracteres especiais 
                    print("Conta criada com sucesso!")
                    break
                else:
                    print("Senha invalida")

            else:
                print("Senha invalida")
                continue

    else:
        print("Usuario invalido")
        continue

    break