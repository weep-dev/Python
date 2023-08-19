
"""     Faça um programa que leia um vetor X[10]. 
        Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.
"""

tam = 10
lista = [0] * tam

for i in range (tam):
    x = int(input())
    if x <= 0:
        lista[i] = 1
    else:
        lista[i] = x
    print("X[{}] = {}".format(i, lista[i]))