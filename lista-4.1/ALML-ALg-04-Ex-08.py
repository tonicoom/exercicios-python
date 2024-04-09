
i = 0
media = 0
valorMaximo = -99999
valorMinimo = 99999

while i < 10:
    numero = int(input("Digite o número: "))
    i+=1

    media += numero
   

    if numero > valorMaximo:
        valorMaximo = numero

    if numero < valorMinimo:
        valorMinimo = numero

print("Maior Valor: ",valorMaximo)
print("Menor Valor: ",valorMinimo)  
media = media /10
print(f"Média: {media:.2f}")