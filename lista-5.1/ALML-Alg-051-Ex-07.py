import random

def sorteia_dado():
    return random.randrange(1, 7)    
rep1 = 0
rep2 = 0
rep3 = 0
rep4 = 0
rep5 = 0
rep6 = 0

for i in range(1000000):
    x = sorteia_dado()
    
    if x == 1:
        rep1 += 1
        
    elif x == 2:
        rep2 += 1
        
    elif x == 3:
        rep3 += 1
        
    elif x == 4:
        rep4 += 1
        
    elif x == 5:
        rep5 += 1
        
    elif x == 6:
        rep6 += 1

        
        
print(f"{rep1 / 1000000 * 100:.2f} % de repetições de 1")
print(f"{rep2 / 1000000 * 100:.2f} % de repetições de 2")
print(f"{rep3 / 1000000 * 100:.2f} % de repetições de 3")
print(f"{rep4 / 1000000 * 100:.2f} % de repetições de 4")
print(f"{rep5 / 1000000 * 100:.2f} % de repetições de 5")
print(f"{rep6 / 1000000 * 100:.2f} % de repetições de 6")

       
       
    

        
        