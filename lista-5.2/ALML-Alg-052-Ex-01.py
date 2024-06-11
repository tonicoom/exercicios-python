import math

def Hipotenusa(c1, c2):
    return math.sqrt((c1 ** 2 + c2 ** 2))

a = int(input("Digite o lado A do triângulo: "))
b = int(input("Digite o lado B do triãngulo: "))

print(f"A Hipotenusa é: ",Hipotenusa(a, b))