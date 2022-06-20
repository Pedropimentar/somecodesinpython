#Crie um script que receba 6 números e retorne quais são os números pares e quais são os ímpares
núm = [[] , []]
valor = 0 
for c in range(1, 7):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor% 2==0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=1' *30)
print(f'Os valores pares digitados são: {núm[0]}')
print(f'Os valores ímpares digitados são: {núm[1]}')