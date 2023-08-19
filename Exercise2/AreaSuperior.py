'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12].
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na 
área superior da matriz, conforme ilustrado abaixo (área verde).
'''

def criar_matriz(lin,col):
  mat = []
  for i in range(lin):
    mat.append([0] * col)
  return mat

def ler_matriz(mat,lin,col):
  for i in range(lin):
    for j in range(col):
      mat[i][j] = float(input())

soma = 0
O = input("")
M = criar_matriz(12,12)
ler_matriz(M, 12, 12)

for i in range (5):
  for j in range (11,0,-1):
    if j > i and j-i >= 1 and i + j < 11:
        soma = soma + M[i][j]

if O == "s" or O == "S":
  print(round(soma, 1))

else:
  print(round(soma/30,1))