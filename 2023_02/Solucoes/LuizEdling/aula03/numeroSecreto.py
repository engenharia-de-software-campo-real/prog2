import random

tentativas = 10
digitos = 3
numeroSecreto = random.randint(0,999)

def main():
    print(f'{numeroSecreto:03d}')
    print(f'Estou pensando num número com {digitos} dígitos com números não repitidos')

if __name__ == '__main__':
    main()