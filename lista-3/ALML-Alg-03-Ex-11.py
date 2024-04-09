import math


a = float(input("Digite o valor a: "))
b = float(input("Digite o valor b: "))
c = float(input("Digite o valor c: "))


discriminante = math.sqrt(b ** 2 - 4 * a * b)

if discriminante < 0:
    print("Não possui raizes reais \n Discriminate: ", discriminante)

elif discriminante == 0:
    equacao = (-b + discriminante ** (1 / 2)) / (2 * a)
    print("Discriminante: ", discriminante)
    print("Valor: ", equacao)
else:
    equacao1 = (-b + discriminante ** (1 / 2)) / (2 * a)
    equacao2 = (-b - discriminante ** (1 / 2)) / (2 * a)
    print("Discriminante: ", discriminante)
    print("Valor positivo: ", equacao1)
    print("Valor negativo: ", equacao2)