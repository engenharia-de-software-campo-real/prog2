'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.
Integrantes do Grupo: Alexandre Lupepsa Brito, Gabriel Penteado
-
-
-
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
# Dados iniciais da conta
saldo_conta = 0 
extrato_conta = []


def verificar_saldo():
    print("Saldo disponível R$ ",round(saldo_conta, 2))


def sacar_dinheiro():
    global saldo_conta #usando global para alterar os valores do saldo da conta em qualquer parte do programa 
    valor_saque = float(input("Digite o valor que deseja sacar R$ "))
    if valor_saque > saldo_conta:
        print("Saldo insuficiente.")
    else:
        saldo_conta -= valor_saque
        extrato_conta.append(f"Saque R$ {round(valor_saque, 2)}") #adicionando um elemento ao final da lista com .append
        

def depositar_dinheiro():
    global saldo_conta
    valor_deposito = float (input("Digite o valor que deseja depositar R$ "))
    saldo_conta += valor_deposito
    extrato_conta.append(f"Depósito R$ {round(valor_deposito, 2)}")

def imprimir_extrato():
    print("Extrato de operações. ")
    for operacao in extrato_conta: 
        print(operacao)

def menu():
    print("\n")
    print("Bem-vindo ao sistema de Caixa Eletrônico")
    print("1 - Verificar saldo da conta")
    print("2 - Sacar dinheiro da conta")
    print("3 - Depositar dinheiro na conta")
    print("4 - Imprimir extrato")
    print("5 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção digitando o número para selecionar: ")

        if opcao == '1':
            verificar_saldo()
        elif opcao == '2':
            sacar_dinheiro()
        elif opcao == '3':
            depositar_dinheiro()
        elif opcao == '4':
            imprimir_extrato()
        elif opcao == '5':
            print("Obrigado por usar o nosso sistema. Volte sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()