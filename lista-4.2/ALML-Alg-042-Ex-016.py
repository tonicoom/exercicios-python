from random import randint
cara = 0
coroa = 0
total = 0

for i in range(10):
    while not abs(cara - coroa) == 3:
        if randint(0, 1) == 0:
            print("A",end="")
            cara +=1
        if randint(0, 1) == 1:
            print("O", end="")
            coroa +=1   
    print(f"({cara + coroa} sorteios)")
    total += cara + coroa
    cara = 0
    coroa = 0

print(f"Na média, foram necessários {(total)/10}")