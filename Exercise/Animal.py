'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
'''

a = input()
b = input()
c = input()

if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
    print('aguia')
elif a == 'vertebrado' and b == 'ave' and c == 'onivoro':
    print('pomba')
elif a == 'vertebrado' and b == 'mamifero' and c == 'onivoro':
    print('homem')
elif a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
    print('vaca')
elif a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
    print('pulga')
elif a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
    print('lagarta')
elif a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
    print('sanguessuga')
elif a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
    print('minhoca')
else:
    print()