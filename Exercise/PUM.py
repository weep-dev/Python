'''
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.
'''

N = int(input())
i = 0
cnt = 1
for i in range(N):
    print (cnt, cnt+1, cnt+2, "PUM")
    cnt = cnt + 4