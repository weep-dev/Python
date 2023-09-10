#Cabeçalho
print("Cadastro")
print("Digite 0 para terminar 0 o cadastro")

cont= 0
lista= []
n= ()
cnt = "s"

#Loop de nomes
while(cnt == "s"):
    n= input(f"Funcionario {cont}")
    lista.append(n)
    cont += 1
    cnt = input("Deseja continuar? ('s' para sim, 'n' para não)")
print(lista)