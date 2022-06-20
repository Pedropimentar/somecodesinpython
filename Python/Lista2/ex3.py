#Simule um radar de rodovia 
#Onde a velocidade máxima permitida na rodovia é 90 Km/h e a mínima 30 Km/h
#-O programa deve capturar a velocidade do usuário por terminal, caso a resposta esteja em branco o programa deve indicar que a velocidade não foi fornecida
#-Caso o usuário esteja abaixo da velocidade o programa deve retornar que o carro está muito lento e que o usuário deve mudar de mão
#-Caso o usuário esteja acima da velocidade o programa deve computar uma multa para o usuário, sendo o valor dessa multa o excesso de velocidade * 7
#-Caso a velocidade não seja fornecida pelo usuário o programa deve sortear um numero entre 1 e 120 e aplicar a mecânica acima com o numero sorteado

from random import randint

Velocidade = float(input('Qual é a velocidade do carro?'))
if Velocidade == 0:
     Velocidade = int(randint(1,120))
if Velocidade > 90:
    multa = (Velocidade-90) * 7
    print('Velocidade excedida!Você excedeu o limite que é de 90 km/h! A sua multa é de R${:.2f}!'.format(multa) )
elif Velocidade < 30:
    print('Você não atingiu a velocidade mínima que é de 30km/h,você está lento. Mude de faixa!')             
print('Tenha uma boa viagem!')