def corretorLetrasMaiusculas(frase):
    frase = str(frase)
    frase = frase.capitalize()
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i - 1] == " ":
            if frase[i - 2] == ".":
                frase[i] = str(frase[i].upper())
            if frase[i - 2] == "!":
                frase[i] = str(frase[i].upper())
            if frase[i - 2] == "?":
                frase[i] = str(frase[i].upper())
    frase = ''.join(frase)
    return print(frase)
             
corretorLetrasMaiusculas("Que horas eu tenho que estar lá? qual é o endereço?")                    