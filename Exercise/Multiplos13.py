'''
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.
'''

X = int((input()))
Y = int((input()))
soma = 0

if X > Y:
    maior = X
    menor = Y
else:
    maior = Y
    menor = X

while menor <= maior:
    if menor % 13 != 0:
        soma = soma + menor
        menor = menor + 1
    else:
        menor = menor + 1

print (soma) 