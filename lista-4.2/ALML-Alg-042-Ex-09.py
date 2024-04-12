
x = float(input("Digite o valor x: "))
raiz = x/2

while raiz * raiz - x > 0.00001:
    raiz = (raiz + x/raiz) /2 
    

print(raiz)
