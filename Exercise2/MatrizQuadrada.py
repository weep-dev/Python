'''
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M 
de inteiros, e construa a matriz de acordo com o exemplo abaixo.
'''

def criar_matriz(lin,col):
  mat = []
  for i in range(lin):
    mat.append([0] * col)
  return mat

def ler_matriz(mat,lin,col):
  for i in range(lin):
    linha = []
    contador = i + 1
    for j in range(col):
        linha.append(abs(contador))
        if(contador == 1):
            mat[i][j] = linha[j]
            contador -= 3
        else:
            mat[i][j] = linha[j]
            contador -= 1
      
def imprimir_matriz(mat, N):
  for i in range(N):
        tx = ''
        for j in range(N):
            tx += " %3d" %mat[i][j]
        print(tx[1:])
  print("")
  

N = int(input())

if 0 <= N <= 100:
  while N != 0:
    mat = criar_matriz(N, N)
    ler_matriz(mat, N, N)
    imprimir_matriz(mat, N)
    N = int(input())