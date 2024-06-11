def hex2int(hexadecimal):
    hexadecimal = str(hexadecimal).upper()
    hexadecimal = list(hexadecimal)
    posicao = 0
    inteiro = 0
    for i in range(len(hexadecimal)):
        if hexadecimal[i] == "A":
            hexadecimal[i] = "10"
        elif hexadecimal[i] == "B":
            hexadecimal[i] = "11"
        elif hexadecimal[i] == "C":
            hexadecimal[i] = "12"
        elif hexadecimal[i] == "D":
            hexadecimal[i] = "13"
        elif hexadecimal[i] == "E":
            hexadecimal[i] = "14"
        elif hexadecimal[i] == "F":
            hexadecimal[i] = "15"
        hexadecimal[i] = int(hexadecimal[i])
        
    for i in range(len(hexadecimal)- 1, -1 , -1):
        hexadecimal[posicao] = hexadecimal[posicao] * (16 ** i)
        inteiro += hexadecimal[posicao]
        posicao +=1
        
    return inteiro
def int2hex(inteiro):
    resultado = inteiro
    tamanho = len(str(inteiro))-1
    hexadecimal = []
    for i in range(tamanho):  
        resto = resultado % 16
        resultado = resultado // 16
        if resto == 10:
            hexadecimal.append("A")
        elif resto == 11:
            hexadecimal.append("B")
        elif resto == 12:
            hexadecimal.append("C")
        elif resto == 13:
            hexadecimal.append("D")
        elif resto == 14:
            hexadecimal.append("E")
        elif resto == 15:
            hexadecimal.append("F")
        else:
            hexadecimal.append(resto)
        hexadecimal[i] = str(hexadecimal[i])     
    hexadecimal = "".join(hexadecimal[::-1])
    return hexadecimal
    


print(int2hex(58028))
print(hex2int("E2AC"))
        
    