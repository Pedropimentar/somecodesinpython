# Simule uma tentativa de criar uma conta em uma plataforma digital
#-O programa deve conferir se a conta do usuário que está sendo criado possui no mínimo 12 caracteres e tenha uma senha que possua de no mínimo 8 caracteres e caracteres numéricos 
#-O programa também deve barrar a entrada de caracteres especiais na criação do nome de usuário
#-O programa só deve criar a conta caso todas as condições tenham sido concluídas, se não o programa deve reiniciar voltando para o primeiro processo
#-Quando a conta for criada o programa deve printar a frase: "conta criada!"

while True:
    nome = (input("Coloque o nome de usuario -> "))
    senha = input("Coloque a senha -> ")

    if len(nome) < 12 and "!" in nome or "#" in nome:
     senha = input("Coloque a senha -> ")
     núm = (1,2,3,4,5,6,7,8,9,0)
     
    if len(senha) <= 8 and not núm in senha and not "!" in senha or not "#" in senha :
        
        break

print("Conta criada!")