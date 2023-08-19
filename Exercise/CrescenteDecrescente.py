'''
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
'''

val1, val2 = map(int, input().split())

while val1 != val2:

    if val1 < val2:
        print("Crescente")
    elif val1 > val2:
        print("Decrescente")
    val1, val2 = map(int, input().split())