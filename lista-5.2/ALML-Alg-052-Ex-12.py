def senhaValida(senha):
    maiuscula = False
    minuscula = False
    temNumero = False
    senha = str(senha)

    if len(senha) < 8:
        return False
 
    for i in range(len(senha)):
        if senha[i] == senha[i].upper():
            maiuscula = True
        if senha[i] == senha[i].lower():
            minuscula = True
        if senha[i].isnumeric() == True:
            temNumero = True
    
        
    if maiuscula == True and minuscula == True and temNumero == True:
        return True
    else:
        return False
     
print(senhaValida("Abcdefg1"))