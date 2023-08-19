def funcao_fora():
    def funcao_dentro():
        print("Eu estou dentro da funcao_dentro")
        
    return funcao_dentro

funcao_aninhada = funcao_fora()

funcao_aninhada()