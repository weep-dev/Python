'''
Ao observar a curva de velocidade de um motor, o engenheiro Zé percebeu que sempre ocorria uma queda quando as medidas eram feitas em intervalos de 10 ms. Mas esta queda acontecia em medidas diferentes a cada novo teste do motor.

Zé ficou curioso com essa falta de padrão e quer saber, para cada teste do motor, qual a primeira medida em que ocorre uma queda de velocidade.
'''

n = int(input())
 
def veloMin(n):
  r = []
  r = input().split()
  q = 0
      
  for i in range(1, n):
      if (int(r[i-1]) > int(r[i])):
          q = i + 1
          return q
  return q

q = veloMin(n)

print(q)