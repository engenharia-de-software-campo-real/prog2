import math
# definicao de uma funcao main
def main():
    # o programa fica aqui dentro 

    peso = float(input("Digigite o seu peso : "))
    altura = float(input("Digite a sua altura: "))

    imc = calcula_imc(peso, altura)

    print(imc)

# nossas próprias funcoes
def calcula_imc(peso, altura):
    imc = peso / pow(altura, 2)
    return imc

# verificador pra rodar o programa
if __name__=='__main__':
    main()
