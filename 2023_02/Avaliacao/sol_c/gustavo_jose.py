'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.

Integrantes do Grupo: 
-Gustavo Ferreira dos Santos
-José Afonso Machado da Cruz
-Luis Gustavo Romanichen Domingues

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

conta_corrente = 0
historico_transacoes = []


def verificar_saldo():
    print(f"Saldo da conta corrente: R${conta_corrente:.2f}")


def sacar():
    global conta_corrente
    valor = float(input("Digite o valor que deseja sacar: R$"))
    if valor <= conta_corrente:
        conta_corrente -= valor
        historico_transacoes.append(f"Saque: -R${valor:.2f}")
        print(f"Você sacou R${valor:.2f} .")
    else:
        print("Saldo insuficiente para realizar o saque.")


def depositar():
    global conta_corrente
    valor = float(input("Digite o valor que deseja depositar: R$"))
    conta_corrente += valor
    historico_transacoes.append(f"Depósito: +R${valor:.2f}")
    print(f"Você depositou R${valor:.2f} .")


def imprimir_extrato():
    print("Extrato de operações:")
    for operacao in historico_transacoes:
        print(operacao)
    verificar_saldo()


while True:
    print("\nMENU:")
    print("1. Verificar saldo da conta corrente")
    print("2. Sacar dinheiro da conta corrente")
    print("3. Depositar dinheiro na conta corrente")
    print("4. Imprimir extrato de operações")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        verificar_saldo()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        imprimir_extrato()
    elif opcao == "5":
        print("Obrigado por usar nosso caixa eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

  # Segue alguns links que usamos de referencia:
  # https://www.guj.com.br/t/exercicio-de-classes/368450      
  # https://python.nilo.pro.br/exercicios3/capitulo%2010/exercicio-10-12.html