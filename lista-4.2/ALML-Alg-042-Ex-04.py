import math
i = True
p = 0.0
x3 = 0.0
y3 = 0.0
x1 = float(input("Digite a cordenada x de um ponto: "))
y1 = float(input("Digite a cordenada y de um ponto: "))
x3 = x1
y3 = y1

while i == True:
    x2 = input("Digite a cordenada x de um ponto (enter para sair): ")
    if x2 == "":
        break
    else: 
        x2 = float(x2)
    
    y2 = float(input("Digite a cordenada y de um ponto:"))

    p += math.sqrt((abs(y2 - y1)** 2) + (abs(x2 - x1)) ** 2)
    x1 = x2
    y1 = y2

p += math.sqrt((abs(y3 - y1)** 2) + (abs(x3 - x1)) ** 2)

print("O perímetro deste polígono é igual a ", p)
    

