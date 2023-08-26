# definicao de uma funcao main
def main():
    # o programa fica aqui dentro 

    peso = input("Digigite o seu peso : ")
    altura = input("Digite a sua altura: ")
    calcula_imc(peso, altura)

    print(calcula_imc)    

# nossas próprias funcoes
def calcula_imc(peso, altura):
    imc = peso / (altura ** 2) 
    return imc

# verificador pra rodar o programa
if __name__=='__main__':
    main()
