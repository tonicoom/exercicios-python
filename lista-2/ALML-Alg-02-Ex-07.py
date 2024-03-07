print("Mostrar dígitos separadamente")
numero = int(input("Digite o número (CDU): "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10 

print("C = ",centena)

print("D = ",dezena)

print("U = ",unidade)


