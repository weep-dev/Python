'''
Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. 
Em cada posição subsequente, coloque o dobro do valor da posição anterior. 
Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. 
Mostre o vetor em seguida.
'''

N = []
X = int(input())
if X <= 50:
    N.append(X)
    for i in range(10):
        N.append(N[-1] * 2)
        print("N[{}] = {}".format(i, N[i]))
else:
    print("Valor precisa ser menor ou igual a 50.")