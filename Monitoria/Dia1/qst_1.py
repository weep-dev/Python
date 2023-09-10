'''
Crie um programa em Python que ajude a decidir qual é o melhor combustivel para abastecer um carro, 
considerando o preço e o rendimento, Peça ao usuário para inserir o preço do etanol e da gasolina, 
bem como o consumo médio do carro com cada um dos combustiveis. 
Com base nas informações, determine se é mais vantajoso abastecer com etanol ou gasolina e 
imprima a decisão.
'''

preco_gas = float(input("Digite o preço da gasolina: "))
preco_etanol = float(input("Digite o preço do etanol: "))

cons_gas = float(input("Digite o consumo do carro com gasolina: "))
cons_etanol = float(input("Digite o consumo do carro com etanol: "))

custo_gas = preco_gas / cons_gas
custo_etanol = preco_etanol / cons_etanol

if custo_gas < custo_etanol:
    print("É mais vantajoso abastecer com gasolina")
elif custo_etanol < custo_gas:
    print("É mais vantajoso abastecer com etanol")
else:
    print("Tanto faz")