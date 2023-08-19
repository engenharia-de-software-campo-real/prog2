def inverte_lista(lista):
    
    lista_invertida = []
    
    for i in range(len(lista)):
        lista_invertida.append(lista[len(lista)-1-i])
    return lista_invertida 


print(inverte_lista([1,2,3,4,5,6,7,8,9,10]))

