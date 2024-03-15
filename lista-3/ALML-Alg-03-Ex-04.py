print("Nomeador de lados poligonais")
lados = int(input("Digite a quantidade de lados do poligono: (03 até 10 lados) "))

if lados >= 3 and lados <=10:
    if lados == 3:
        print("Triângulo")
    elif lados == 4:
        print("Quadrado")
    elif lados == 5:
        print("Pentágono")
    elif lados == 6:
        print("Hexágono")
    elif lados == 7:
        print("Heptágono")
    elif lados == 8:
        print("Octógono")
    elif lados == 9:
        print("Eneágono")
    elif lados == 10:
        print("Decágono")
else:
    print("Erro")


