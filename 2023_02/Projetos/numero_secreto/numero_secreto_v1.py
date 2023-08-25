# imports
import random 

NUMERO_PRA_ADIVINHAR = 123

# escopo do programa
def main():
    print(
        '''Estou pensando em um numero de 3 digitos, tente adivinhar qual é!'''
    )
    # coleto a entrada do usuario e atribuo a uma variavel
    numero_usuario = int(input("Digite o numero que eu estou pensando: "))

    # verifico o numero que o usuario entrou
    if numero_usuario == NUMERO_PRA_ADIVINHAR:
        print("Você Acertou!!")
    else:
        print("Você Errou!!")

# incializador do programa
if __name__ == '__main__':
    main()