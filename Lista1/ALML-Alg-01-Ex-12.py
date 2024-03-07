import math

print("Área e Volume")
raio = float(input("Raio: "))

area = math.pi * (raio ** 2)

volume = (4/3) * (math.pi ** 3)

print(f"Área: {area:.2f}",)
print(f"Volume: {volume:.2f}")