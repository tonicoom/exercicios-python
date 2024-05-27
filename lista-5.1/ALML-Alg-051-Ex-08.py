def numero_digitos(n):
    rep = 0 
    if n > 0:
        n = str(n)
        rep = len(n)
        return print(rep)
    else:
        print("O número deve ser maior que zero")


numero_digitos(4)

numero_digitos(4020)

numero_digitos(400323232)