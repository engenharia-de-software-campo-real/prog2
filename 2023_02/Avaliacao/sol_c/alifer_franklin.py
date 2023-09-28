
'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.
Integrantes do Grupo:

-Alifer Ruan S. Schiomo
-João Victor D. Guerra
-guilherme amaral
-franklin vargas

Instruções:
0. Faca uma cópia desse arquivo para que você desenvolva sua solução
1. Após terminar, publique sua solução no classroom na atividade da prova
Problema:
Seu grupo foi contratado para desenvolver um aplicativo para um caixa eletrônico
de banco.
Seu aplicativo deve conter as seguintes funcionalidades:
- Um menu com opçoes para o usuário
- Verificar saldo da conta corrente
- Sacar dinheiro da conta corrente
- Depositar dinheiro na conta corrente
- Printar extrato de operacoes de deposito e saque da conta
'''

def main():

    import random
    conta = 0
    saldo = 50000
    extrato = []
    sacar = 0
    deposito = 0

    while conta <1:
        conta = int(input("\nInsira o numero de cinco digitos do seu cartao/conta:"))
    

    opcao = int(input("\nselecione a opcao:\n1-MOSTRAR SALDO DA CONTA:\n2-SACAR:\n3-DEPOSITAR\n4-extrato\n"))

    if opcao == 1:

        print(saldo)
        main()

    if opcao == 2:
        print(saldo)

        while sacar != -1:
            sacar=int(input("informe o valor do saque (digite -1 para sair):"))
            if sacar == -1:
                main()
            if sacar > 0 & sacar <= saldo:
                print("\nSaque concluido, retire seu dinheiro.")

                print("\nseu saldo restante eh:",saldo - sacar)
                main()
            if sacar > saldo:
                print("voce nao pode sacar um valor maior que seu saldo!!")


    if opcao == 3:
        print(saldo)
        while deposito != -1:
            deposito=int(input("informe o valor do deposito (digite -1 para sair):"))

            print("\nDeposito concluido.")

            print("\nseu saldo atual eh:",saldo + deposito)
            main()


    if opcao == 4:
        print(saldo)

        print(extrato)



    
main()
# if __name__ == '__main__':
#     main()
main.py
