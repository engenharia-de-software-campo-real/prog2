# Avaliação 1° bimestre - Programação 2
# Professor: Pedro Lealdino Filho, PhD.

# Bruno Braga de Moura Breitwisser
# Nathaly Vitoria Hoffmann Maia de Oliveira
# Luis Otávio Op. Radek

# Sites utilizados:
# https://www.devmedia.com.br/funcoes-em-python/37340
# como pular linha no python


def main():
    saldoInicial = 0.0;
    novoSaldo = 0.0;
    extratos = [];
    print("Bem-vindo ao app bancário!");
    menu(saldoInicial, novoSaldo, extratos);


def menu(saldoInicial, novoSaldo, extratos):
    print("----------------------");
    print("O que gostaria de fazer?\n");
    print("1- Verificar saldo");
    print("2- Sacar dinheiro");
    print("3- Depositar dinheiro");
    print("4- Retirar extrato\n");
    print("----------------------");
    opcao = input();
    opcaoescolhida(opcao, saldoInicial, novoSaldo, extratos);

def fecharApp(saldoInicial, novoSaldo, extratos):
  print("-------------------");
  print("Deseja realizar uma nova operação?");
  print("1 - SIM");
  print("2 - NÃO");
  close = int(input());
  if(close == 1):
    menu(saldoInicial, novoSaldo, extratos);
  else:
    print("App encerrado com sucesso!");
    exit();

def opcaoescolhida(opcao, saldoInicial, novoSaldo, extratos):
  if(opcao == "1"):
    print("-------------------");
    print("Seu saldo atual é de ", novoSaldo);
    fecharApp(saldoInicial, novoSaldo, extratos);
  elif(opcao == "2"):
      print("-------------------");
      print("Qual valor deseja sacar?");
      valorDoSaque = float(input());
      if(valorDoSaque > novoSaldo):
        print("-------------------");
        print("Erro! Valor do saque é maior que saldo disponível!");
        fecharApp()
      else:
        extratos.append("Saque efetuado");
        novoSaldo -= valorDoSaque;
        print("-------------------");
        print("Saque efetuado com sucesso! seu novo saldo é de ", novoSaldo);
        fecharApp(saldoInicial, novoSaldo, extratos)
  elif(opcao == "3"):
    print("-------------------");
    print("Digite quanto deseja depositar em sua conta");
    valorDoDeposito = float(input());
    novoSaldo += valorDoDeposito;
    extratos.append("Deposito efetuado");
    print("-------------------");
    print("operação realizada com sucesso! seu novo saldo é de ", novoSaldo);
    fecharApp(saldoInicial, novoSaldo, extratos)
  elif(opcao == "4"):
    print("-------------------");
    print("Aqui está seu extrato de operações bancárias:");
    print(extratos);
    fecharApp(saldoInicial, novoSaldo, extratos);
  else:
    print("----------------------");
    print("Opção inválida, tente novamente!");
    menu();


if __name__ == '__main__':
    main()