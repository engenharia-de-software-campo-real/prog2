def dar_ola(nome):
    
    string_retornada = "Ola, " + nome + "!"
    
    return string_retornada

nome = str(input("Digite seu nome: "))

print(dar_ola(nome))
