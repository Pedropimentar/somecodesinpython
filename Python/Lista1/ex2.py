from msilib.schema import CustomAction
Custo_F = int(input("Coloque o custo de Fabrica: ")) 
c_distribuicao = (Custo_F/72)*100
c_impostos= (Custo_F/55)*100
print(f"(O Custo total do carro será: {Custo_F + c_distribuicao + c_impostos}")