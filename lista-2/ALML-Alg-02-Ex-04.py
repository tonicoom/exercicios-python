import math

print("Ordenação de três inteiros (menor para o maior)")

n1 = int(input("1º Inteiro: "))
n2 = int(input("2º Inteiro: "))
n3 = int(input("3º Inteiro: "))

menorValor = min(n1,n2,n3)
maiorValor = max(n1,n2,n3)

valorMeio = (n1 + n2 + n3) - (menorValor + maiorValor)

print(f"Menor valor: {menorValor}")
print(f"Maior valor: {maiorValor}")
print(f"Valor do meio: {valorMeio}")
