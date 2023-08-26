# importar

# defino funcoes
def testa_par(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


# inicio do programa
valor_teste = testa_par(int(input("a: ")))
outro_valor = testa_par(int(input("b: ")))

if valor_teste == outro_valor:
    print("os valores sao iguais")
else:
    print("os valores sao diferentes")