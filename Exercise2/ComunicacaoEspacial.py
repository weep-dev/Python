'''
O ano é 2337. Milhares de naves de tripulações humanas viajam pelo espaço de forma alucinada para lá e para cá. E o melhor: as naves conseguem se comunicar através de rádio, é possível até mesmo que tripulações entre naves distintas jogarem truco.

No entanto, infelizmente a qualidade do sinal esvanece com a distância. Enquanto naves próximas conseguem se comunicar bem, as naves que estão distantes possuem péssima intensidade de sinal para se comunicar. Por esse motivo, as naves comunicam-se preferencialmente com a nave mais próxima.

Considerando um trecho do espaço onde as naves podem ser consideradas pontos no espaço, portanto com coordenadas tridimensionais, com cada eixo podendo ter valor entre 0 e 100 u.m. Sabe-se que a intensidade do sinal de comunicação se dá pela distância entre as naves; de modo que naves que distam entre si até 20 u.m. possuem uma intensidade alta; acima de 20 u.m. e até 50 u.m. possuem uma intensidade média; enquanto a intensidade do sinal acima de 50 u.m. é tão baixa que não possibilita a comunicação entre as naves.

Dadas as informações passadas, ajude os tripulantes destas naves a conseguirem saber a intensidade do sinal entre cada uma delas e a nave mais próxima, para informá-los se eles vão conseguir ter uma boa comunicação entre si.
'''

import math

def calcular_distancia(nave1, nave2):
    x1, y1, z1 = nave1
    x2, y2, z2 = nave2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def determinar_intensidade_sinal(naves):
    intensidades = []

    for i, nave1 in enumerate(naves):
        menor_distancia = float('inf')
        for j, nave2 in enumerate(naves):
            if i != j:
                distancia = calcular_distancia(nave1, nave2)
                if distancia < menor_distancia:
                    menor_distancia = distancia
        if menor_distancia <= 20:
            intensidades.append('A')
        elif menor_distancia <= 50:
            intensidades.append('M')
        else:
            intensidades.append('B')

    return intensidades

# Leitura das naves
N = int(input())
naves = []
for _ in range(N):
    x, y, z = map(int, input().split())
    naves.append((x, y, z))

# Determinar intensidade do sinal para cada nave
resultado = determinar_intensidade_sinal(naves)

# Imprimir resultados
for intensidade in resultado:
    print(intensidade)