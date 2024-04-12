q = int(input("Digite um número decimal: "))
result = ""

while q != 0:
    r = q % 2
    r = str(r)
    result = result + r
    q = q // 2

print(result)