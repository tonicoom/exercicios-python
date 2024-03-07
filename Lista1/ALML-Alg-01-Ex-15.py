import math

print("Área de um polígono regular")

lado = float(input("Comprimento dos lados dos triângulos: "))

n = float(input("Quantidade de lados: "))

area = (n * lado**2) / 4 * math.atan(math.pi/n)

print(f"{area:.2f}")


