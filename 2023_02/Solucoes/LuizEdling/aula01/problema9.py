funcionario = input('Digite o número do funcionário: ')
horas = float(input('Digite as horas trabalhadas: '))
vphora = float(input('Digite o quanto ele recebe por hora trabalhada: '))
salário = horas*vphora
print(f'Funcionário: {funcionario}\nSalário: {salário:.2f}')
