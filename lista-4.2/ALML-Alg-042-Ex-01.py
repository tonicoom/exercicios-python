media = 0
contador = 0
nota = 1

while nota != 0:
    nota = int(input(f"Digite a {contador + 1}º nota (Para encerrar o programa digite 0): "))
    contador += 1
    if nota != 0:
        media += nota
    else:
        break

media = media / (contador - 1)

print(f"Sua média é: {media} ")