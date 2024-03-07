import math
print("1º Cordenada")
t1 = math.radians(float(input("Latitude: ")))
g1 = math.radians(float(input("Longitude: ")))

print("2º Cordenada")
t2 = math.radians(float(input("Latitude: ")))
g2 = math.radians(float(input("Longitude: ")))


distancia = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
# t = latitude g = longitude
print(f"{distancia:.2f} km")

