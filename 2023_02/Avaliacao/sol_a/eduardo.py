def menu():
    print("="*70)
    print("Bem-vindo ao Sistema de Gerenciamento de Vendas e Estoque de Veículos")
    print("="*70)
    print("1. Verificar estoque de veículos")
    print("2. Registrar um veículo")
    print("3. Vender um veículo")
    print("4. Exibir controle de finanças")
    print("5. Sair")


def main():
    estoque = {}


    controle_financeiro = {
        'vendas': [],
        'compras': []
    }
    while True:
        menu()
        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            print("Estoque de veículos:")
            for veiculo, quantidade in estoque.items():
                print(f"{veiculo}: {quantidade} unidades")


        elif opcao == "2":
            veiculo = input("Digite o nome do veículo: ")
            quantidade = int(input("Digite a quantidade a ser adicionada ao estoque: "))
            estoque[veiculo] = estoque.get(veiculo, 0) + quantidade
            print(f"{quantidade} unidades de {veiculo} adicionadas ao estoque.")


        elif opcao == "3":
            veiculo = input("Digite o nome do veículo a ser vendido: ")
            quantidade = int(input("Digite a quantidade a ser vendida: "))


            if veiculo in estoque and estoque[veiculo] >= quantidade:
                estoque[veiculo] -= quantidade


                preco_venda = float(input("Digite o preço de venda por unidade: "))
                custo = float(input("Digite o custo por unidade: "))
                lucro = (preco_venda - custo) * quantidade
                controle_financeiro['vendas'].append({
                    'veiculo': veiculo,
                    'quantidade': quantidade,
                    'preco_venda': preco_venda,
                    'custo': custo,
                    'lucro': lucro
                })
                print(f"{quantidade} unidades de {veiculo} vendidas com sucesso.")


            else:
                print("Estoque insuficiente.")


        elif opcao == "4":
            print("Controle de Finanças:")
            for venda in controle_financeiro['vendas']:
                print(f"Veículo: {venda['veiculo']}, Quantidade: {venda['quantidade']}, "
                      f"Preço de Venda: {venda['preco_venda']}, Custo: {venda['custo']}, Lucro: {venda['lucro']}")


        elif opcao == "5":
            print("Obrigado por usar o Sistema de Gerenciamento de Vendas e Estoque de Veículos.")
            break


        else:
            print("Opção inválida. escolha uma opção válida.")


if __name__ == '__main__':
    main()