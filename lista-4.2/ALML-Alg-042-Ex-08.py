frase = input("Digite a sua frase:")
distancia = int(input("Digite a distância: "))
fraseNova = ""

for i in range(0, len(frase)):
    fraseNova += chr(ord(frase[i]) + distancia)

print(fraseNova)