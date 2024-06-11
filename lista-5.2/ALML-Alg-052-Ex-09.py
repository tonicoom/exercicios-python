def isInteger(string):
    tamanhoString = len(string)
    string = str(string).split()
    string = str(string)
    
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numerosTotais = 0
    for i in range(len(string)):
        for k in range(len(numeros)):
            if string[i] == numeros[k]:
                numerosTotais +=1
    
    if numerosTotais == tamanhoString:
        return True
    else:
        return False
            
               
    
print(isInteger("adada"))
        