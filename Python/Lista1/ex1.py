
anos = int(input("Digite sua idade em anos ->"))
meses = int(input("Em quantos meses ->"))
dias = int(input("E quantos dias ->"))

quant_anos = anos * 365
quant_meses = meses * 30

total = dias + quant_anos + quant_meses

print(f"A sua idade total em dias e igual a: {total} dias")