print("Soma dos quatro dígito")
numero = int(input("Digite o número (quatro dígitos): "))

primeiroDigito = numero // 1000
segundoDigito = (numero % 1000) // 100
terceiroDigito = (numero % 1000) % 100 // 10
quartoDigito = (numero % 1000) % 100 % 10

somaDigitos = primeiroDigito + segundoDigito + terceiroDigito + quartoDigito

print("A soma dos dígitos é igual a: ", somaDigitos)



