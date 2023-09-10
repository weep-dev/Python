print("Operação - Adição")
#Inicia Operação
op=str(input("Quer realizar a Operação; S/N\n"))

#Loop
while (op == "S"):
    
    num1= float(input("Numero 1: "))
    num2= float(input("Numero 2: "))

    soma= num1 + num2

    print(f"{num1:.2f} + {num2:.2f} = {soma:.2f}\n")
    
    #Loop ou End
    op= str(input("Quer realizar a Operação novamente? S/N: \n"))