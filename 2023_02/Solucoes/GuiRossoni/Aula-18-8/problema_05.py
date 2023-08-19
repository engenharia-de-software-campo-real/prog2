def recursiva(n):
    if n == 1:
        return 1
    else:
        return n * recursiva(n-1)

num = int(input("Digite um numero: "))    
    
print(recursiva(num))