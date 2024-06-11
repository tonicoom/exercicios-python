def baseaParaBase10(numero, base):
    
    decimal = 0
    digitos = "0123456789ABCDEF"
    
    numero = numero.upper()[::-1]

    for i, digito in enumerate(numero):
        decimal += digitos.index(digito) * (base ** i)

    return decimal
    
print(baseaParaBase10("13ABD", 16))    
    
def base10ParaBasea(numero, base):
    digitos = "0123456789ABCDEF"
    resultado = ""

    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero //= base

    return resultado      
    
    