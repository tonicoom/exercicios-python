def ehPrimo(numero):
    numero = int(numero)
    numerosDivisiveis = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            numerosDivisiveis += 1
    if numerosDivisiveis == 2:
        return True
    else:
        return False

print(ehPrimo(13))
            