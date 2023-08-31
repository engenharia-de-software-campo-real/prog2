import random #importando uma biblioteca 

NUM_DIGITS = 3 
MAX_GUESSES = 10 

def main():
    print(''' 
          Número Secreto é um jogo de Adivinhação!
          
          Estou pensando em um número com {} dígitos com números não repetidos. 
          Você tem {} tentativas!
          Tente adivinhar qual é o número. Aqui vão algumas dicas:
          Quando eu digo:   Isso significa:
          Pico              Um dígito está correto mas na posição errada
          Fermi             Um dígito está correto e na posição correta
          Bagels            Nenhum dígito está correto

          Por exemplo, se o número secreto for 248 e seu chute for 843, a dica será
          Fermi Pico.'''.format(NUM_DIGITS, MAX_GUESSES))
    
    while True:
        numero_secreto = pega_numero_aleatorio()
        print('Eu pensei em um número')
        print('Você tem {} chances para tentar acertar.'.format(MAX_GUESSES))

        numero_de_chutes = 1
        while numero_de_chutes <= MAX_GUESSES:
            chute = ''
            while len(chute) != NUM_DIGITS or not chute.isdecimal():
                print('Chute #{}: '.format(numero_de_chutes))
                chute = input('> ')

            dicas  = pega_dicas(chute, numero_secreto)
            print(dicas)
            numero_de_chutes += 1

            if chute == numero_secreto:
                break 
            if numero_de_chutes > MAX_GUESSES:
                print('Voce esgotou suas tentativas: ')
                print('A resposta era {}.'.format(numero_secreto))
            
        print('Você quer jogar de novo?! (sim ou nao)')
        if not input('> ').lower().startswith('y'):
            break
    print('Obrigado por jogar!')

def pega_numero_aleatorio():

    numeros = list('0123456789')
    random.shuffle(numeros)
    
    numero_secreto = ''
    for i in range(NUM_DIGITS):
        numero_secreto += str(numeros[i])

    return numero_secreto

def pega_dicas(chute, numero_secreto):
    if chute == numero_secreto:
        return "Você Venceu!"
    
    dicas = []

    for i in range(len(chute)):
        if chute[i] == numero_secreto[i]:
            dicas.append('Fermi')

        elif chute[i] in numero_secreto:
            dicas.append('Pico')

    if len(dicas) == 0:
        return 'Bagels'
    else:
        dicas.sort()

        return ' '.join(dicas)
            

# voces nao precisam entender o porque disso, soh precisa ter, aceitem!
if __name__ == '__main__':
    main()