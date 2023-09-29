# '''
# Avaliacao : 1 bimestre - Programacao 2 
# Professor: Pedro Lealdino Filho, PhD.
# Turma: A

# Integrantes do Grupo: 
# - Anne Gabrielly Latchuk Antunes
# - Guilherme Rossoni
# - Rubens Ricardo Santana

# Instrucoes:

# 0. Faca uma copia desse arquivo para que voce desenvolva sua solucao
# 1. Antes terminar, publique sua solucao no classroom na atividade da prova

# Problema:

# Seu grupo foi contratado para desenvolver um aplicativo gerenciamento de vendas
# e estoque para uma revenda de veiculos online. 

# Seu aplicativo deve conter as seguintes funcionalidades:

# - Um menu com opcoes para o usuario
# - Verificar estoque de veiculos: crie um estoque ficticio
# - Registrar um veiculo
# - Vender um veiculo
# - Adicionar o valor de venda do veiculo em um controle de financas, o seu custo e o lucro obtido
# - Printar um demonstrativo de todas as vendas e compras dos veiculos 


# '''
def main():
    #Estoque de veiculos e variaveis de controle financeiro
    estoque = {

        "Gol": {
            "quantidade": 3,
            "preco_compra": 5000.0,
            "preco_venda": 7500.0
        },
        "Fusca": {
            "quantidade": 2,
            "preco_compra": 5000.0,
            "preco_venda": 6500.0
        },
        "Opala": {
            "quantidade": 1,
            "preco_compra": 10000.0,
            "preco_venda": 15000.0
        },
    }
    ControleFinanceiro = {"ReceitaTotal":0, "CustoTotal": 0, "LucroTotal": 0}

    #Funcao para impresssao do estoque ao usuario, foi utilizado uma fomatacao de string para ponto flutuante com duas casas decimais para melhor visualizacao
    #Fonte da formatacao: https://www.pythonpool.com/python-float-to-string/
    def ControleEstoque():
        
        if not estoque:
            print("\nNenhum veiculo no estoque.")
        else:    
            print("\nEstoque de veiculos:")
            for veiculo, info in estoque.items():
                print(f"\n{veiculo}: {info['quantidade']} unidades - Custo: R${info['preco_compra']:.2f} - Valor de Venda: R${info['preco_venda']:.2f}")

    #Funcao para cadastro de veiculos
    def CadastroVeiculo():
        veiculo = input("\nDigite o modelo do veiculo: ")
        quantidade = int(input("\nDigite a quantidade a ser registrada: "))
        preco_compra = float(input(f"\nDigite o custo de compra de cada {veiculo}: "))
        preco_venda = float(input(f"\nDigite o valor de venda de cada {veiculo}: "))
        
        if veiculo in estoque:
            estoque[veiculo]["quantidade"] += quantidade
        else:
            estoque[veiculo] = {
                "quantidade": quantidade,
                "preco_compra": preco_compra,
                "preco_venda": preco_venda
            }

    #Funcao para venda de veiculos
    def VendaVeiculo():
        veiculo = input("\nDigite o modelo do veiculo a ser vendido: ")
        if veiculo in estoque:
            quantidade = int(input(f"\nDigite a quantidade de {veiculo} a ser vendida: "))
            if quantidade <= estoque[veiculo]["quantidade"]:
                preco_venda = estoque[veiculo]["preco_venda"]
                custo = estoque[veiculo]["preco_compra"]
                receita = quantidade * preco_venda
                custo_total = quantidade * custo
                lucro = receita - custo_total

                estoque[veiculo]["quantidade"] -= quantidade
                ControleFinanceiro["ReceitaTotal"] += receita
                ControleFinanceiro["CustoTotal"] += custo_total
                ControleFinanceiro["LucroTotal"] += lucro

                print(f"\n{quantidade} unidades de {veiculo} foram vendidas.")
            else:
                print(f"\nNao ha {quantidade} unidades de {veiculo} disponiveis no estoque.")
        else:
            print(f"\n{veiculo} nao esta no estoque.")

    #Funcao para impressao do controle financeiro ao usuario, foi utilizado uma fomatacao de string para ponto flutuante com duas casas decimais para melhor visualizacao
    #Fonte da formatacao: https://www.pythonpool.com/python-float-to-string/
    def MostrarControleFinanceiro():
        print("\nControle Financeiro:")
        print(f"\nReceita Total: R${ControleFinanceiro['ReceitaTotal']:.2f}")
        print(f"Custo Total: R${ControleFinanceiro['CustoTotal']:.2f}")
        print(f"Lucro Total: R${ControleFinanceiro['LucroTotal']:.2f}")
    
    #O loop foi usado para a impressao do menu e para a chamada das funcoes
    while True:
        print("\nMenu:")
        print("\n1. Verificar Estoque")
        print("2. Registrar Veiculo")
        print("3. Vender Veiculo")
        print("4. Resumo do Controle Financeiro")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opcao: ")
        
        if opcao == '1':
            ControleEstoque()
        elif opcao == '2':
            CadastroVeiculo()
        elif opcao == '3':
            VendaVeiculo()
        elif opcao == '4':
            MostrarControleFinanceiro()
        elif opcao == '5':
            break
        else:
            print("\nOpcao invalida!")
            
if __name__ == '__main__':
    main()