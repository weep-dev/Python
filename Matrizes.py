#Funcoes para matrizes

def criar_matriz(lin, col):
    mat = []
    for i in range(lin):
        mat.append([0] * col)
    return mat

def ler_matriz(mat, lin, col):
    for i in range(lin):
        for j in range(col):
            mat[i][j] = int(input("Digite um numero: "))

def imprimir_matriz(mat, lin, col):
    for i in range(lin):
        for j in range(col):
            print(mat[i][j]," ", end="",)
        print()

def somar_matriz(mat1, mat2, lin, col):
    soma = criar_matriz(lin, col)
    for i in range(lin):
        for j in range(col):
            soma[i][j] = mat1[i][j] + mat2[i][j]
    return soma

def matriz_transposta(mat, lin, col):
    matTransp = criar_matriz(col, lin)
    for i in range(lin):
        for j in range(col):
            matTransp[j][i] = mat[i][j]
    return matTransp

def encontrar_valor(mat, lin, col, valor):
    for i in range(lin):
        for j in range(col):
            if mat[i][j] == valor:
                return [i, j]
    return []

gabarito = ['a', 'd', 'c', 'a', 'b', 'e', 'c', 'a', 'd', 'b']

provas = [['a', 'd', 'c', 'a', 'c', 'e', 'a', 'a', 'd', 'b'], ['a', 'a', 'c', 'a', 'b', 'e', 'c', 'a', 'd', 'b'], ['a', 'a', 'a', 'c', 'b', 'e', 'c', 'a', 'd', 'b'], ['a', 'd', 'c', 'a', 'b', 'd', 'd', 'd', 'd', 'd'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']]


for i in range(5):
    nota = 0
    for j in range(10):
        if provas[i][j] == gabarito[j]:
            nota += 1
    print(f'O aluno {i+1} tirou uma nota {nota}')