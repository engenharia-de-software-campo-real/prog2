import random

NUM_DIGITS = 3
MAX_GUESSES = 10 

def main():
    print(''' 
          Número Secreto é um jogo de Adivinhação!
          
          Estou pensando em um número com {} dígitos com números não repetidos. 
          Tente adivinhar qual é o número. Aqui vão algumas dicas:
          Quando eu digo:   Isso significa:
          Pico              Um dígito está correto mas na posição errada
          Fermi             Um dígito está correto e na posição correta
          Bagels            Nenhum dígito está correto

          Por exemplo, se o número secreto for 248 e seu chute for 843, a dica será
          Fermi Pico.'''.format(NUM_DIGITS))
    
if __name__ == '__main__':
    main()