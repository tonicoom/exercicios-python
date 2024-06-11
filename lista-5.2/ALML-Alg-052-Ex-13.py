def quantosDias(mes, ano):
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ano = str(ano)
    if mes > 12 or mes < 1:
        return False
    if len(ano) != 4:
        return False
    if ehBisexto(ano) == True:
        meses[1] = 29
    mes = mes - 1
    return meses[mes]
def ehBisexto(ano):
    ano = int(ano)
    
    if ano % 400 == 0:
        return True
    
    elif ano % 100 == 0:
        return False

    elif ano % 4 == 0:
        return True

    else:
        return False

print(quantosDias(2, 2024))