n = int(input("Digite o número n: "))
a = 0
p = 2

for i in range(1, n+1):
    a += 1 / ((2 * p) - 1)
    p += 2

    

print(a)