def conta_digitos(n, d):
    if 0 <= d <= 9:
        n = str(n)
        d = str(d)
        rep = 0

        for i in range(len(n)):
            if n[i] == d:
                rep += 1
        return rep
    else:
        print("Erro: a segundo argumento deve ser um número entre 0 e 9")

print(conta_digitos(101, 5))