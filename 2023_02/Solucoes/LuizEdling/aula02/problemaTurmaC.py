import random
import string

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

# def descriptografado(palavra):
#     texto = []
#     for caractere in palavra:
#         texto.append(ord(caractere))
#     metade = len(texto)//2    
#     for i in range(metade, len(texto)):
#         texto[i] = texto[i] + 1
#     texto.reverse()

#     for i in range(0, len(texto)):
#         if(((caractere)>=65 and (caractere)<=90) or ((caractere)>=97 and (caractere)<=122)):
#             texto[i] = ((caractere)-3)
#         else:
#             texto[i] = ((caractere)-3)
#     for i in range(len(texto)):
#         if texto[i] < 32:  
#             texto[i] += 95
#         texto[i] = chr(texto[i])
#     textoDescriptografado = ''.join(texto)
#     return textoDescriptografado

def descriptografado(palavra):
     texto = []
     for caractere in palavra:
         texto.append(ord(caractere))
     metade = len(texto) // 2
     for i in range(metade, len(texto)):
         texto[i] = texto[i] + 1
     texto.reverse()
    
     texto_descriptografado = []
     for caractere in texto:
         if ( (caractere >= 65 and caractere <= 125)):
             texto_descriptografado.append(caractere - 3)
         else:
             texto_descriptografado.append(caractere)
            
     for i in range(len(texto_descriptografado)):
         if texto_descriptografado[i] < 32:  
             texto_descriptografado[i] += 95
         texto_descriptografado[i] = chr(texto_descriptografado[i])
        
     texto_descriptografado = ''.join(map(str,texto_descriptografado))
     return texto_descriptografado


def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

for i in range(1104):
    string = random_generator()
    print(f'--------------STRING {i}--------------\n')
    print(criptografado(string))
    print(descriptografado(criptografado(string)))
    print('------------------------------------\n')





    
