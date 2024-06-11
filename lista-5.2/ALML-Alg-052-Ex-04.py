def mediana(a, b, c):
    lista = [a, b, c]
    lista.sort()
    return lista[1]

    
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

medianaResultado = mediana(num1, num2, num3)
print("A mediana dos valores é:", medianaResultado)
