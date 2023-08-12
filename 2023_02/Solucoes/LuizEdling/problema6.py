while(True):
    A = float(input('Digite a primeira nota do aluno (de 0 a 10.0): '))
    B = float(input('Digite a segunda nota do aluno (de 0 a 10.0): '))
    if((A<1 or A>10) or (B<1 or B>10)):
        print('Notas inválidas, tente novamente\n')
    else:
        break
m = float(((A*3.5)+(B*7.5))/11)
print(f'MEDIA = {m:.5f}')
