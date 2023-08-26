def main():

    def criptografado(palavra):
        texto = []
        for caractere in palavra:
            if((ord(caractere)>=65 and ord(caractere)<=90) or (ord(caractere)>=97 and ord(caractere)<=122)):
                texto.append(ord(caractere)+3)
            else:
                texto.append(ord(caractere))
            
        texto.reverse()
        metade = len(texto)//2
        for i in range(metade, len(texto)):
            texto[i] = texto[i] - 1
        for i in range(len(texto)):
            if texto[i] < 32:  
                texto[i] += 95
            texto[i] = chr(texto[i])
        textoCriptografado = ''.join(texto)
        return textoCriptografado

    def descriptografado(palavra):
        texto = []
        for caractere in palavra:
            texto.append(ord(caractere))
        metade = len(texto)//2    
        for i in range(metade, len(texto)):
            texto[i] = texto[i] + 1
        texto.reverse()
        for caractere in texto:
            if(((caractere)>=65 and (caractere)<=90) or ((caractere)>=97 and (caractere)<=122)):
                texto.append((caractere)-3)
            else:
                texto.append((caractere))
        for i in range(len(texto)):
            if texto[i] < 32:  
                texto[i] += 95
            texto[i] = chr(texto[i])
        textoDescriptografado = ''.join(texto)
        return textoDescriptografado

    print(descriptografado('3# rvzgV'))

if __name__ == '__main__':
    main()


    
