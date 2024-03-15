nomeDaNota = input("Digite o nome da nota: ")

letra = nomeDaNota[:1]
numero = int(nomeDaNota[1:2])

if letra == "C":
    frequencia = 261.63
    resultado = frequencia / 2 ** (4 - numero)

elif letra == "D":
    frequencia = 293.66
    resultado = frequencia / 2 ** (4 - numero)

elif letra == "E":
    frequencia = 329.63
    resultado = frequencia / 2 ** (4 - numero)

elif letra == "F":
    frequencia = 349.23
    resultado = frequencia / 2 ** (4 - numero)

elif letra == "G":
    frequencia = 392.00
    resultado = frequencia / 2 ** (4 - numero)

elif letra == "A":
    frequencia = 440.00
    resultado = frequencia / 2 ** (4 - numero)

elif letra == "B":
    frequencia = 493.88
    resultado = frequencia / 2 ** (4 - numero)

print(resultado," Hz")

