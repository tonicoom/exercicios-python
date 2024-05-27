def encaixa(a, b):
    a = str(a)
    b = str(b)

    return a[-len(b): ] == b

maior = None
menor = None

a = input("Digite um valor a: ")
b = input("Digite um valor b: ")

if len(a) > len(b):
    maior = a
    menor = b
elif len(b) > len(a):
    maior = b
    menor = a

for i in range(len(maior)):
    if encaixa(maior[:i], menor) == True:
        print(True)

