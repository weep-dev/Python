'''
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
'''

n = 1
p = 0
num = 1
den = 1
S = 0

while n < 40:
    S = S + num/den
    num = num + 2
    den = den * 2
    n = n + 1
print(f"{S:.2f}")