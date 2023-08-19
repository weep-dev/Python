'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.
'''

N= int(input())
i = 0
dentro = 0
fora = 0
for i in range(N):
    X = int(input())
    if 10 <= X <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print (dentro, "in")
print (fora, "out")