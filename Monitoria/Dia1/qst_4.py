'''
Crie um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.
 Tipo
Faixa (KWh)
Preço
Residencial
Até 500 Acima de 500
R$ 0,40 R$ 0,65
Comercial
Até 1000 Acima de 1000
R$ 0,55 R$ 0,60
Industrial
Até 5000 Acima de 5000
R$ 0,55 R$ 0,60
'''

consumo = float(input("Digite quantos kWh é consumido: "))
tipo = input("Digite o tipo de consumo (R/residências, I/indústrias e C/comércios): ")
total_pagar = 0
preco = 0

if (tipo == "R"):
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60

total_pagar = consumo * preco

print(f"Valor total a se pagar {total_pagar}")