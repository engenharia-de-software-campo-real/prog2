def quadrado(n):
    return n**2

def nova_lista(lista, funcao):
        novaLista = []
        for elemento in lista:
            novaLista.append(funcao(elemento))
        return novaLista
lista = [1,2,3,4,5]
print(nova_lista(lista, quadrado))
