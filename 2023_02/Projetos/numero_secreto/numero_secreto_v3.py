# imports
import random 

NUMERO_PRA_ADIVINHAR = 123
NUMERO_DE_TENTATIVAS = 10

# escopo do programa
def main():
    print(
        '''Estou pensando em um numero de 3 digitos, tente adivinhar qual é!'''
    )

    while True:

        numero_usuario = int(input("Digite o numero que eu estou pensando: "))

        verifica_chute(numero_usuario)

        break
    

# declaracao de funcoes
def verifica_chute(numero_do_chute):
    
    if numero_do_chute == NUMERO_PRA_ADIVINHAR:
        print("Você Acertou!!")
    else:
        print("Você errou!!!")


# incializador do programa
if __name__ == '__main__':
    main()