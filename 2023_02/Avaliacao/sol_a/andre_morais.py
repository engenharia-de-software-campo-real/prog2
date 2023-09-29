'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.
Turma: A

Integrantes do Grupo: 
-
-
-
-
-

Instruções:

0. Faca uma cópia desse arquivo para que você desenvolva sua solução
1. Após terminar, publique sua solução no classroom na atividade da prova

Problema:

Seu grupo foi contratado para desenvolver um aplicativo gerenciamento de vendas
e estoque para uma revenda de veículos online. 

Seu aplicativo deve conter as seguintes funcionalidades:

- Um menu com opçoes para o usuário
- Verificar estoque de veículos: crie um estoque fictício
- Registrar um veículo
- Vender um veículo
- Adicionar o valor de venda do veículo em um controle de finanças, o seu custo e o lucro obtido
- Printar um demonstrativo de todas as vendas e compras dos veículos 
- prof aprendi a usar o global com o chat gpt para poder fazer a alteração ao adicionar mais um veículo no estoque

'''
marcaV1 = "Civic 2016"
precoV1 = 60000
marcaV2 = {}
precoV2 = {}
lucro = ""
def main():
    menu()

def menu():
    
    print("***********************")
    print("*        MENU         *")
    print("*                     *")
    print("* 1-VERIFICAR ESTOQUE *")
    print("* 2-REGISTRAR VEICULO *")
    print("* 3-VENDER VEICULO    *")
    print("* 4-FINANCEIRO        *")
    print("* 5-RELATORIO         *")
    print("*                     *")
    print("***********************")
    escolha = int(input(print("\nESCOLHA UMA OPCAO: ")))
    if escolha == 1:
        estoque()

    elif escolha == 2:
        registro()

    elif escolha == 3:
        vender()

    elif escolha ==4:
        financeiro()

    elif escolha ==5:
        relatorio()

def estoque():
    print("\n{} R$ {}".format(marcaV1,precoV1))
    print("\n {} R$ {}".format(marcaV2,precoV2))
    escolha2 = int(input(print("Aperte '0' para voltar ao menu")))
    if escolha2 == 0 :
        menu()

def registro():
    global marcaV2 
    marcaV2 = str(input("\nDigite a marca do veiculo: "))
    global precoV2 
    precoV2 = float(input("\nDigite o preco do veiculo: "))
    escolha3 = int(input(print("Aperte '0' para voltar ao menu")))
    if escolha3 == 0 :
        menu()
        
        

def vender():
    print("\n 1- {} R$ {}".format(marcaV1,precoV1))
    print("\n 2- {} R$ {} \n".format(marcaV2,precoV2))
    venda = int(input(print("Selecione qual deseja vender (ou '0' para voltar ao menu): ")))
    if venda == 1:
        print("Vendido!")
        menu()

    elif venda == 2:
        print("Vendido!")
        menu()
    else:
        menu()

def financeiro():
    comissao = precoV2 * 0.2
    lucro = precoV2 - comissao
    print("Relatorio Financeiro")
    print("Seu valor total anunciado a venda eh {}".format(precoV2))
    print("O valor total da comissao do site eh {}".format(comissao))
    print("Seu lucro pós venda é {}".format(lucro))
    escolha9 = int(input(print("Aperte '0' para voltar ao menu")))
    if escolha9 == 0 :
        menu()
 

def relatorio():
    print("Seu total vendido até hoje é de R$ 50.000,00")
    print("Seu carro vendidos são \n Corsa 2012 R$ 25.000,00 \n Celta 2012 R$ 25.000,00")
    print("O valor total comissionado ao site eh de R$ 10.000,00")
    print("Seu lucro total ate hojee eh de R$ 40.000,00")
    escolha8 = int(input(print("Aperte '0' para voltar ao menu")))
    if escolha8 == 0 :
        menu()
if __name__ == '__main__':
    main()