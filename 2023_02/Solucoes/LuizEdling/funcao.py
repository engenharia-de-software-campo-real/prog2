

def calculadora(op,n1,n2):
    if(op == 1):
        return n1+n2
    if(op == 2):
        return n1-n2
    if(op == 3):
        return n1*n2
    if(op == 4):
        valor = float(n1)/float(n2)
        valorf = f'{valor:.2f}'
        return valorf
    

op = int(input('Escolha a operação\n[1] SOMA\n[2] SUBTRAÇÃO\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\n'))
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if(op==1):
    opf = 'soma'
if(op==2):
    opf = 'subtração'
if(op==3):
    opf = 'multiplicação'
if(op==4):
    opf = 'divisão'
print(f'A {opf} entre {n1} e {n2} é {calculadora(op,n1,n2)}')
        