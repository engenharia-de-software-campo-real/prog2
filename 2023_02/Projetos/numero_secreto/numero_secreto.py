import random #importando uma biblioteca 

NUM_DIGITS = 3 
MAX_GUESSES = 10 
NUM = 145 #exemplo mais simples

def main():
    print(''' 
          N�mero Secreto � um jogo de Adivinha��o!
          
          Estou pensando em um n�mero com {} d�gitos com n�meros n�o repetidos. 
          Voc� tem {} tentativas!
          Tente adivinhar qual � o n�mero. Aqui v�o algumas dicas:
          Quando eu digo:   Isso significa:
          Pico              Um d�gito est� correto mas na posi��o errada
          Fermi             Um d�gito est� correto e na posi��o correta
          Bagels            Nenhum d�gito est� correto

          Por exemplo, se o n�mero secreto for 248 e seu chute for 843, a dica ser�
          Fermi Pico.'''.format(NUM_DIGITS, MAX_GUESSES))
    
    controle_de_execucao = 0

    while True:
        numero_do_usuario = str(input("Digite um numero com tr�s digitos: "))

        controle_de_execucao += 1

        if verifica_numero_valido(numero_do_usuario):
            verifica_igualdade(numero_do_usuario)
        
        if controle_de_execucao > MAX_GUESSES:
            break

        #como verificar as posicoes dos numeros do usuario com o numero pra adivinhar?
    
# defino todas minhas funcoes 
def verifica_numero_valido(numero):
    if len(numero) == 3:
        # print("o numero eh valido")
        return True
    else:
        # print("o numero nao eh valido")
        return False

def verifica_igualdade(numero):
    if numero == NUM:
        print("voce acertou")
    else:
        print("voce errou")


# voces nao precisam entender o porque disso, soh precisa ter, aceitem!
if __name__ == '__main__':
    main()