'''
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.
'''

nota1 = float(input())
while  10 < nota1 or nota1 < 0:
    print ("nota invalida")
    nota1 = float(input())

nota2 = float(input())
while  10 < nota2 or nota2 < 0:
    print ("nota invalida")
    nota2 = float(input())

media = (nota1 + nota2) / 2
print ("media = {:.2f}".format(media))
