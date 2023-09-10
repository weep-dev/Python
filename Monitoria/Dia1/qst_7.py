nt1 = float(input("informe uma nota:"))
nt2 = float(input("informe outa nota:"))
media = (nt1 + nt2)/2

if media == 10:
    print ("APROVADO COM DISTINÇÃO")
elif media < 7:
    print ("REPROVADO")
elif media >= 7:
    print("APROVADO")
else:
    ("...")