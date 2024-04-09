n = int(input("Digite o número n: "))
a = 1

for i in range(1, n+1):
    if i % 2 == 0:
        a += 1 / i
    else:
        a -= 1/ i

print(a)