valor_hora = float(input("Qual o valor da hora de trabalho: "))
horas = int(input("Quantas horas trabalhadas no mes: "))

salarioBruto = valor_hora * horas

fgts = 0.11 * salarioBruto
sindicato = 0.03 * salarioBruto
importoR = 0

if 900 < salarioBruto <= 1500:
    importoR = 0.05 * salarioBruto
elif salarioBruto <= 2500:
    importoR = 0.10 * salarioBruto
elif salarioBruto > 2500:
    importoR = 0.20 * salarioBruto

descontos = sindicato + importoR
salarioLiquido = salarioBruto - descontos

print("Salário Bruto: ", salarioBruto)
print("Imposto de Renda: ", importoR)
print("Sindicato: ", sindicato)
print("FGTS: ", fgts)
print("Total de descontos: ", descontos)
print("Salário Liquido: ", salarioLiquido)
