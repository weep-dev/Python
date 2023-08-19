'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
'''

inicio, fim = map(int, input().split())

if inicio >= fim:
    duracao = 24 - inicio + fim
else:
    duracao = fim - inicio

print(f'O JOGO DUROU {duracao} HORA(S)')