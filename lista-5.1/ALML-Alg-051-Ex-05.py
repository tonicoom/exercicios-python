def potencia(x, y):
    z = x
    for i in range(1, y):
        x *= z  
        
    return x

print(potencia(5, 3))
print(potencia(2, 3))
print(potencia(7, 10))

