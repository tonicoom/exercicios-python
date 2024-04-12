palavra = "a"

while palavra != "":
    palavra = input("Digite sua palavra: ").lower()

    for i in range(len(palavra)):
        primeira = palavra[0]
        segunda = palavra[1]

        penultima = palavra[len(palavra)- 2]
        ultima = palavra[len(palavra)- 1]

    if primeira is ultima and segunda is penultima:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
    

