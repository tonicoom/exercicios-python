def trianguloValido(lado1, lado2, lado3):
    maior = max(lado1, lado2, lado3)
    menores = (lado1 + lado2 + lado3) - maior

    if maior >= menores:
        print("Não é um triângulo válido")
    else:
        print("É um triângulo válido")


trianguloValido(12, 8, 15)