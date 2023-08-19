def soma_multiplos(*args):
    soma = 0
    for i in args:
        soma += i
    return soma


print(soma_multiplos(10,10,10,10,10,10))


