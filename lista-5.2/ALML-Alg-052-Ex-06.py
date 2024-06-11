def centralizandoString(string, largura):
    linhas = []

    for i in range(largura):
        svTamanhoLista = len(linhas)
        linhas.append(" ")

    linhas.append(string)
    linhas = ''.join(linhas)
    print(linhas)    

centralizandoString("tubaina", 10)