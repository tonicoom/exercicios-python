posicao = input("Digite a posição do tabuleiro: ").lower()

coluna = posicao[0:1]
linha = int(posicao[1:2])

if coluna == "a":
        if (linha % 2) != 0:
                print("Casa preta")
        else:
                print("Casa branca")
        

elif coluna == "b":
        if (linha % 2) == 0:
                print("Casa branca")
        else:
                print("Casa branca")


elif coluna == "c":
        if (linha % 2) != 0:
                print("Casa preta")
        else:
                print("Casa branca")

elif coluna == "d":
        if (linha % 2) == 0:
                print("Casa branca")
        else:
                print("Casa branca")

elif coluna == "e":
        if (linha % 2) != 0:
                print("Casa preta")
        else:
                print("Casa branca")

elif coluna == "f":
        if (linha % 2) == 0:
                print("Casa branca")
        else:
                print("Casa branca")
elif coluna == "g":
        if (linha % 2) != 0:
                print("Casa preta")
        else:
                print("Casa branca")

elif coluna == "h":
        if (linha % 2) == 0:
                print("Casa branca")
        else:
                print("Casa branca")
