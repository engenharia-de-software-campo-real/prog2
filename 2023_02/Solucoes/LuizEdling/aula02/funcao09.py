def funcaoDentro():
        mensagem = 'mensagem'
        return mensagem

def funcaoFora():
    return funcaoDentro()
print(funcaoFora())