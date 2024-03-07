import math
print("Área do triângulo (novamente)")

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

lado = (lado1 + lado2 + lado3) / 2
area = math.sqrt(lado * (lado - lado1) * (lado - lado2) * (lado - lado3))

print(f"{area:.2f}")


