'''
Faça um programa para um caixa de mercado que imprima um recibo de compras. 
O programa deve receber o nome de N produtos que estão sendo comprados (N simboliza uma quantidade variada). 
Utilize as estruturas de repetição.

Também deve receber as informações de quantidade e valor unitário de cada um destes produtos.

Exiba o valor total de cada produto comprado e o valor total das compras de todos os produtos.
'''
total_compras = 0
produtos = []

num = int(input("Quantos produtos: "))

for i in range(num):
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor = float(input("Digite o preço por unidade: "))

    valor_total = valor * quantidade

    produtos.append((nome_produto, quantidade, valor, valor_total))

    total_compras = total_compras + valor_total

print("Recibo das compras: ")
print("-------------------------")

for i in range(num):
    print(produtos[i])

print(f"O valor total foi de {total_compras} reais")
