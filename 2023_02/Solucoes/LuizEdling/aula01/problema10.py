vendedor = input('Digite o nome do vendedor: ')
salário = float(input(f'Digite o salário do {vendedor}: '))
vendas = int(input(f'Digite quantas vendas {vendedor} fez: '))*100
finalMes = ((vendas*15)/100)+salário
print(f'Funcionário irá receber {finalMes:.2f} no final do mês')