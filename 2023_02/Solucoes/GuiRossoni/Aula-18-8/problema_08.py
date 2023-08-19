
def funcao(n):
    return n ** 3

def aplica_funcao(lista, funcao):
    nova_lista = []
    for i in lista:
        nova_lista.append(funcao(i))
    return nova_lista

lista = [1, 2, 3, 4, 5]

print(aplica_funcao(lista, funcao))

