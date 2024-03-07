print("Mostrar dígitos separadamente")
m = int(input("Digite o número (CDU - UDC): "))
# 321

u = m // 100
d = (m % 100) // 10 * 10 
c = ((m % 100) % 10) * 100

print(int(u + d + c))
