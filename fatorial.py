#Fatorial de um numero utilizando uma funcao recursiva

def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1)
    
x = fatorial(5)
print(x)