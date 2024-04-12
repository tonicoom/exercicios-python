aproximacao = int(input("Digite a aproximação do pi que deseja: "))
pi = 3
a = 2
b = 3
c = 4
i = 1

while i != aproximacao:
    i+=1
    pi += 4 / (a * b * c) 
    a +=2
    b +=2
    c +=2
print(pi)
    
    
