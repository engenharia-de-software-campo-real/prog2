def potencia(x,y):
    
    potencia = lambda x, y: x ** y
    
    return potencia(x,y)

x = int(input("Digite da base: "))
y = int(input("Digite do expoente: "))

print(potencia(x,y))