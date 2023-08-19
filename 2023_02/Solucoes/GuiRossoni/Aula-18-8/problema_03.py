def par_ou_impar(numero):
    
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
    
numero = int(input("Digite um numero: "))

print(par_ou_impar(numero))
    
