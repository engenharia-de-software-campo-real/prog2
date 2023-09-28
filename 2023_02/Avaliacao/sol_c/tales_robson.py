'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.

Integrantes do Grupo: 
- tales Ribeiro
- Guilherme Eduardo
- Robson Keller

- Um menu com opçoes para o usuário //, Primeiramente pede o Nome do usuario e seu saldo, Usa 3 ifs para o menu. Sendo "Digite 1 para Verificar Saldo" 
- Verificar saldo da conta corrente //"Digite 2 para 2 Opções. Sacar ou Depositar Dinheiro". "Digite 3 para Printar Extrato"
- Sacar dinheiro da conta corrente // "NA OPÇÃO 2, quando DEPOSITAR, colocar na variavel [Dinheiro+DinColocado]. Quando Sacar colocar [Dinheiro-DinColocado]
  //"a variável de dinheiro precisa ser a mesma a ser lida no printar, adicionando Dinheiro<-Dinheiro(Sacado[+] ou Depositado(-))"
- Depositar dinheiro na conta corrente // "O valor de deposito e o valor de saque são separados"
- Printar extrato de operacoes de deposito e saque da conta

'''
saldo = 0
extrato = []

def verificar_saldo():
    return saldo

def sacar(valor):
    global saldo
    if valor <= 0:
        return "O saque deve ser maior que zero."
    if valor > saldo:
        return "Saldo insuficiente."
    saldo -= valor
    extrato.append(f"Saque: - R${valor:.2f}")
    return f"Saque de R${valor:.2f}"

def depositar(valor):
    global saldo
    if valor <= 0:
        return "O depósito deve ser maior que zero. "
    saldo += valor
    extrato.append(f"Depósito: + R${valor:.2f}")
    return f"Depósito de R${valor:.2f} "

def imprimir_extrato():
    print("Extrato de Operações:")
    for operacao in extrato:
        print(operacao)

def main():
    nome = input("Digite o seu nome: ")
    print(f"Bem-vindo, {nome}!")

    while True:
        print("\nEscolha uma opção:")
        print("1 -Verificar saldo")
        print("2 -Sacar dinheiro")
        print("3 -Depositar dinheiro")
        print("4 -Imprimir extrato")
        print("5 -Sair")

        escolha = input("Digite A Opção ")

        if escolha == "1":
            saldo_atual = verificar_saldo()
            print(f"Seu saldo atual é de: R${saldo_atual:.2f}")
        elif escolha == "2":
            valor_saque = float(input("Quanto você gostaria de sacar: R$"))
            resultado = sacar(valor_saque)
            print(resultado)
        elif escolha == "3":
            valor_deposito = float(input("Quanto você gostaria de depositar: R$"))
            resultado = depositar(valor_deposito)
            print(resultado)
        elif escolha == "4":
            imprimir_extrato()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Número Inválido, tente 1,2,3,4 ou 5")

if __name__ == "__main__":
    main()