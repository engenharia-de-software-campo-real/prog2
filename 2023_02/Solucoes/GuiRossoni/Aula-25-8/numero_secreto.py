import random

NUM_DIGITS = 3
MAX_GUESSES = 10 

lista_numeros = [random.randint(0, 9) for _ in range(3)] #GERADOR DE NUMEROS ALEATORIOS
lista_numeros_str = ''.join(map(str, lista_numeros))

NUM = lista_numeros_str

print("Debug resposta: " ,NUM)

def main():
    print(''' 
          Numero Secreto e um jogo de Adivinhacao!
          
          Estou pensando em um numero com {} digitos com numeros nao repetidos. 
          Voce tem {} tentativas!
          Tente adivinhar qual e o numero. Aqui vao algumas dicas:
          Quando eu digo:   Isso significa:
          Pico              Um digito esta correto mas na posicao errada
          Fermi             Um digito esta correto e na posicao correta
          Bagels            Nenhum digito esta correto

          Por exemplo, se o numero secreto for 248 e seu chute for 843, a dica sera
          Fermi Pico.'''.format(NUM_DIGITS, MAX_GUESSES))
    
    controle_de_tentativas = 0
    
    while True:
        
        controle_de_tentativas += 1 #CONTADOR DE TENTATIVAS
        
        numero_secreto = str(input("\nDigite um numero de tres digitos: "))
        print("\n")
    
        if verifica_numero(numero_secreto):
            verifica_igualdade(numero_secreto)
            posicao_dos_numeros(numero_secreto)
            
        if controle_de_tentativas == MAX_GUESSES:   
            break
        
        if verifica_igualdade(numero_secreto) == True:
            print("\nVoce acertou o numero secreto!\n")
            break
        
        if not verifica_igualdade(numero_secreto):
            print("\nVoce errou o numero secreto!\n")
    
def posicao_dos_numeros(numero_secreto): #COMPARADOR PARA OS NUMEROS INFORMADOS E PRESENTES NA VARIAVEM NUM
    for i in range(len(numero_secreto)):
        if numero_secreto[i] == NUM[i]:
            print("Fermi")

        elif numero_secreto[i] in NUM:
            print("Pico")

        else:
            print("Bagels")  
    
def verifica_numero(numero_secreto): #VERIFICADOR ADIGIONAL PARA ENTRADAS MENORES QUE 3 DIGITOS
    if len(numero_secreto) != NUM_DIGITS:
        print("\nO numero precisa conter 3 digitos!")
        return False
    
    else:
        return True
    
def verifica_igualdade(numero_secreto): #VERIFICADOR PARA COMPARAR O NUMERO INFORMADO COM A VARIAVEL NUM
    if numero_secreto == NUM:
        return True   
    
    else:
        return False
        
if __name__ == '__main__':
    main()