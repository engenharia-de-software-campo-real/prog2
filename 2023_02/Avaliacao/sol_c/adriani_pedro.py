'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.

Integrantes do Grupo: 
PEDRO LUCAS TERNOPILSKI LUBINA
ADRIANI DELFINO 

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
    def saque(valor_saque: float, saldo: float):
        saldo = saldo - valor_saque
        transacoes.append(('saque', valor_saque))
        return saldo

    def deposito(valor_deposito: float, saldo: float):
        saldo = saldo + valor_deposito
        transacoes.append(('deposito', valor_deposito))
        return saldo
    
    def extrato():
        for transacao in transacoes:
            print(transacao[0] + ": " + str(transacao[1]))
        print("saldo: " + str(saldo))

    saldo = 1000
    transacoes = []

    while True:
        print("Visualizar saldo da conta, digite saldo")
        print("Realizar deposito bancário, digite deposito")
        print("Realizar saque bancário, digite saque")
        print("Visualizar extrato da conta, digite extrato")
        print("Para sair, digite sair")
        resposta = input("Qual operação deseja fazer?")

        if resposta == 'saldo':
            print(f"O valor do seu saldo atual é: {saldo}")
        elif resposta == 'saque':
            valor_saque = float(input('Qual o valor que deseja sacar?'))
            saldo = saque(valor_saque, saldo)
            print(f"O valor do seu saldo atual é: {saldo} ")

        elif resposta == 'deposito':
            valor_deposito = float(input('Qual o valor que deseja depositar?'))
            saldo = deposito(valor_deposito, saldo)
            print(f"O valor do seu saldo atual é: {saldo} ")
        elif resposta == 'extrato':
            extrato()
        elif resposta() == 'sair':
            break

if __name__ == '__main__':
    main()