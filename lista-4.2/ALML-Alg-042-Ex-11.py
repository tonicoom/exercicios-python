import re
frase_ao_contrario = []

frase = input("Digite a frase: ")
frase = ''.join(frase.split())
frase = re.sub('[.,!?]', '', frase)

for i in range(len(frase),0 , -1):
    frase_ao_contrario.append(frase[i-1])

frase_nova = ''.join(frase_ao_contrario).lower()
frase = frase.lower()

if frase_nova == frase:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

print(frase_nova)
print(frase)