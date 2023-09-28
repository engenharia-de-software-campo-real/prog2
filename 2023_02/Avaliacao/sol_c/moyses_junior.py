
#Avaliacao : 1 bimestre - Programacao 2 
#Professor: Pedro Lealdino Filho, PhD.

#Integrantes do Grupo: 
#Instruções:

#0. Faca uma cópia desse arquivo para que você desenvolva sua solução
#1. Após terminar, publique sua solução no classroom na atividade da prova

#Problema:

#Seu grupo foi contratado para desenvolver um aplicativo para um caixa eletrônico
#de banco.

#Seu aplicativo deve conter as seguintes funcionalidades:

#- Um menu com opçoes para o usuário
#- Verificar saldo da conta corrente
#- sacar dinheiro da conta corrente

# - Depositar dinheiro na conta corrente
#- Printar extrato de operacoes de deposito e saque da conta

def main():

    while True:
        lista_extrato = []
        print("CONFIRA O MENU ABAIXO")
        print("Digite 1 para verificar o saldo da conta")
        print("Digite 2 para sacar dinheiro da conta corrente")
        print("Digite 3 para depositar dinheiro da conta corrente")
        print("Digite 4 para eextrato")
        print("Digite 0 para sair")

        saldo = 0.0

        opcao = input()

        if opcao == "1":
            verificar_saldo(saldo)
        elif opcao == "2":
            sacar(saldo)
        elif opcao == "3":
            depositar(saldo, lista_extrato)
        elif opcao == "4":
            extrato(lista_extrato)
        elif opcao == "0":
            print("Saindo do programa.")
            exit()
        else:
            print("digite um numero valido")
               

def verificar_saldo(saldo):
    print('seu saldo é', saldo)

def sacar(saldo, lista_extrato):
    print('qunbato quer sacar:')
    saca = float(input())
    saldo -= saca
    print('ase3u noiv saldo pe de ', saldo)
    lista_extrato.append("saque")

def depositar(saldo, lista_extrato):
    print('qunbato quer depositar:')
    depo = float(input())
    saldo += depo
    print('ase3u noiv saldo pe de ', saldo)
    lista_extrato.append("depositar")

def extrato(lista_extrato):
    print(lista_extrato)


    


        

if __name__ == "__main__":
 main()