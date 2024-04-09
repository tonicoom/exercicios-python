i = True
media = 0
valorMaximo = -99999
valorMinimo = 99999

while i == True:

    numero = str(input("Digite o número: "))
    if numero == "":
        break

    numero = int(numero)
    
    media += numero

    if numero > valorMaximo:
        valorMaximo = numero

    if numero < valorMinimo:
        valorMinimo = numero


print("Maior Valor: ",valorMaximo)
print("Menor Valor: ",valorMinimo)  

media = media /10

print(f"Média: {media:.2f}")