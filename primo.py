#Verificacao de numero primo

def primo(n):
    for numero in range(2,n):
        if(n % numero == 0):
            return False
    return True

n = int(input("Digite um numero: "))
primo = primo(n)
print(primo)