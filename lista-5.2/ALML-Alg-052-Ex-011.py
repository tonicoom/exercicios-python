import random
def gerarSenha():
    senha = []
    comprimentoAleatorio = random.randrange(7, 11, 1)
    for i in range(comprimentoAleatorio):
        letraASCI = chr(random.randrange(33, 127, 1))
        senha.append(letraASCI)
        
    senha = "".join(senha)
    print(senha)
    
gerarSenha()
gerarSenha()
gerarSenha()
gerarSenha()
gerarSenha()
gerarSenha()
        
        