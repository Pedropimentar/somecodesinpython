#Crie um jogo RPG por turnos de console
#-O programa deve permitir o usuário à escolher entre dois personagens (mago ou guerreiro)
#Caso o usuário escolha guerreiro o programa deve sortear um valor aleatório entre 5 e 10 que será a barra de poder do guerreiro 
#Caso o usuário escolha mago o programa deve sortear um valor aleatório entre 7 e 15 que será a barra de poder do mago
#-Dentro do jogo o usuário terá 4 opções:
#Atacar (sorteia um valor de 3 a 10 de dano caso o usuário tenha escolhido guerreiro ou sorteia um valor entre 0 e 8 caso o usuário tenha escolhido um mago, independente do personagem escolhido o jogador gasta 2 de poder por ataque)
#Defender (cancela 1 ataque do inimigo, caso o usuário seja um mago o jogador gasta 1 de poder de ataque), 
#Curar (cura 1 de vida no caso do guerreiro e 2 de vida no caso do mago)
#Descansar (sorteia um valor entre 1 e 5 e usa este valor para recuperar pontos de poder)
#-Monstros
#Os monstros são gerados com 20 de vida
#Para atacar o monstro em seu turno escolhe aleatoriamente entre atacar dando 3 de dano ou se defender
#Quando algum monstro é morto, o usuário tem a opção de sair do jogo ou continuar
#Caso o usuário após matar um monstro queira continuar jogando, toda a sua vida é recuperada e o próximo monstro gerado terá 10 de vida e 3 de ataque a mais que o último e o jogador ganhará mais 3 de probabilidade de ataque e mais 5 de vida

import time
from random import randint

vida_monstro = 20
vida = 16

#start
print("Seja bem-vindo ao jogo do século! Encare essa aventura como sua longa estrada da vida! ")
time.sleep(2.0)
personagem = input(" É chegada a hora da sábia escolha de seu personagem, pense bem, pois sua vida depende dessa escolha!Escreva: 1-> Guerreiro 2-> Mago")
time.sleep(2.0)


while True:
    if not "Mago" in personagem and not "Guerreiro" in personagem:
        continue
    break

while True:
    #Guerreiro
    if personagem == "Guerreiro":
    

        personagem == "Guerreiro"
        time.sleep(2.0)
        acao = input("Escolha sua ação: \n 1- Atacar \n 2- Defender \n 3- Curar \n 4- Descansar:")
        if  not "Atacar" in acao or not "Defender" in acao or not "Curar" in acao or not "Descansar" in acao:
         atacar = randint(3, 10)
        ataque_monstro = 3
        vida = 16
        cura = vida + 1
        descansar = randint(1,5)
        poder = randint(5, 10)

        if acao == "Atacar":
            poder -= 2
            vida -= ataque_monstro
            vida_monstro -= atacar
            print(f"Sua vida: {vida}. \n O dano do ataque foi: {atacar} \n A vida do Monstro: {vida_monstro} \n Ataque do Monstro foi: {ataque_monstro}")
        
        elif acao == "Defender":
            poder-= 1
            print(f"A sua vida é: {vida} \n A vida do monstro é: {vida_monstro}")

        elif acao == "Curar":
            vida += cura
            vida -+ ataque_monstro
            print(f"A sua vida é: {vida} \n O dano de ataque foi: {atacar} \n O ataque do monstro foi: {vida_monstro}")

        elif acao == "Descansar":
            poder += cura
            vida -+ ataque_monstro
        else:
            print("Digite novamente,por favor!!")
    else: 
        #Mago
        personagem =="Mago"
        time.sleep(2.0)

        acao = input("Escolha sua acao: \n 1- Atacar \n 2- Defender \n 3- Curar \n 4- Descansar: ")
        if  not "Atacar" in acao or not "Defender" in acao or not "Curar" in acao or not "Descansar" in acao:
            atacar = randint(0,8)
            ataque_monstro = 3
            vida = 16
            cura = vida + 2
            descansar = randint(1,5)
            poder = randint(5,10)

            if acao == "Atacar":
                poder -= 2
                vida -=  ataque_monstro
                vida_monstro -= atacar
                print(f"Sua vida: {vida}. \n O dano do ataque foi: {atacar} \n A vida do Monstro: {vida_monstro} \n Ataque do Monstro foi: {ataque_monstro}")

            elif acao == "Defender":
                poder -= 1   
                print(f"A sua vida é: {vida} \n A vida do monstro é: {vida_monstro}")
        
            elif acao == "Curar":  
                vida += cura
                vida -= ataque_monstro
                print(f"A sua vida é: {vida} \n O dano de ataque foi: {atacar} \n O ataque do monstro foi: {vida_monstro}")

            elif acao == "Descansar":
                poder += descansar
                vida -= ataque_monstro
            else:
                print("Por favor digite novamente")   

        if vida <= 0:
            print ("Você morreu, gamer over")
            while True:
                resposta = input("Você morreu, deseja jogar novamente?")

                if resposta == "Sim":
                    break
                elif resposta == "Nao":
                    break
                else: 
                    continue

            print ("Que pena! Só os fortes ganham")

            if resposta == "Sim":
                vida_do_monstro = 20
                vida = 13
                continue
            else:
                break

        if vida_do_monstro <= 0:
            while True:
                resposta = input("Você matou o monstro, quer enfrentar outro?")

                if resposta == "Sim":
                    break
                elif resposta == "Nao":
                    break
                else: 
                    continue

            print ("Parabens! Você ganhou o monstro morreu")

            if resposta == "Sim":
                vida_do_monstro = 10
                continue
            else:
                break
        



    



        


