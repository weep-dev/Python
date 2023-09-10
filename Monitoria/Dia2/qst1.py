"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
"""
n1 = float(input("Digite o preço do produto 1: "))
n2 = float(input("Digite o preço do produto 2: "))
n3 = float(input("Digite o preço do produto 3: "))

if n2 > n1 < n3:
    print("O produto mais barato é o produto 1")
elif n1 > n2 < n3:
    print("O produto mais barato é o produto 2")
else:
    print("O produto mais barato é o produto 3")
    
