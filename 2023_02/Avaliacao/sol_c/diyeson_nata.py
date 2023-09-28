
'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.
Integrantes do Grupo: 

- Dyeison Felipe Kreuz
- Natãn Teixeira Vieira
- Ruan Kysã Mendes Bueno
- Renann Felipe Volff
- João Mateus Rosa Machado

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
    saldo = 0
    depositar = 0
    extrato_dep = []
    extrato_sac = []
    valor = 0
    

    print("Bem vindo ao banco central")

    while True:
        
         
        print("escolha uma opção: ")
        print("(1)verificar saldo")
        print("(2)sacar dinheiro")
        print("(3) depositar dinheiro")
        print("(4) extrato bancário")
        print("(5)Sair")
        opcao = int(input("opcao: "))

        if opcao == 1:
            print("Seu saldo é de R$ %.2f" % saldo)
            
        elif opcao == 2:
            while True:
                saque = float(input(" Valor do saque R$: "))
                if(saque <= saldo):
                    print("saque disponivel")
                    sal = int(input("comfirmar saque ? 1-S/2-N: "))
                    if sal == 1:
                        print("saque realidado no valor de R$",saque)
                        extrato_sac.append(saque)
                        break    
                    elif sal == 2:
                        print("saque cancelado")
                        break
                if(saque >= saldo):
                    print("saldo indisponivel")

        elif opcao == 3:
            depositar = float(input('Digite o depósito inicial: R$'))
            print(f'Depósito de R$ {depositar:.2f}')
            saldo = depositar
            extrato_dep.append(depositar)

        elif opcao == 4:
            print("saldo: %.2f" % saldo)
            print("quantidade_de_saqueS:", extrato_sac)
            print("quantidade_de_depositos:", extrato_dep)
            
        elif opcao == 5:
            break
        else:
            print("opção invalida! ")
    print("Operação encerrada!! tenha um otimo dia.")           


if __name__ == '__main__':
    main()

Prova.py
Exibindo Prova.py…