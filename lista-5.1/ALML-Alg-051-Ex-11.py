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

a = input("Digite o valor inteiro positivo a: ")
b = input("Digite o valor inteiro positivo b: ")
numeros = [1,2,3,4,5,6,7,8,9]
repeticoesA = []
repeticoesB = []


for k in range(9):
    repeticoesA.append(conta_digitos(int(a), numeros[k]))

for k in range(9):
    repeticoesB.append(conta_digitos(int(b), numeros[k]))
    
if repeticoesA == repeticoesB:
    print("É uma permutação")
else:
    print("Não é uma permutação")

print(repeticoesA)
print(repeticoesB)