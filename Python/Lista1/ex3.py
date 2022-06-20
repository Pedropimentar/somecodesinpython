Total_Eleitores= int(input("Digite o Número total de eleitores: "))

Total_Nulos= int(input("Digite o número de votos nulos:"))

Total_Brancos= int(input("Digite o Número total de votos brancos:"))

Total_Validos= int(input("Digite o Número total de Votos Válidos:"))

Percentual_nulos= (Total_Eleitores/Total_Nulos)*100
Percentual_Brancos= (Total_Eleitores/Total_Brancos)*100
Percentual_Validos= (Total_Eleitores/Total_Validos)*100

print(f" O percentual de votos em Branco é: {Percentual_Brancos}")

print(f" O percentual de votos em Branco é: {Percentual_nulos}")

print(f" O percentual de votos em Branco é: {Percentual_Validos}")