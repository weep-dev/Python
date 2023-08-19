'''
Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, 
um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso.
A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação.
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
    
M = criar_matriz(12, 12)

L = int(input(""))
T = input("")
ler_matriz(M, 12, 12)


if T == "s" or T == "S":
  print(sum(M[L]))

elif T == "m" or T == "M":
  print(round(sum(M[L])/12, 1))