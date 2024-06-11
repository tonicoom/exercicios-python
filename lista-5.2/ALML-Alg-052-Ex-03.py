def valorTotalEnvio(quantidadePedidos):
    precoEnvio = 10.95

    while quantidadePedidos > 1:
        quantidadePedidos -= 1
        precoEnvio += 2.95

    return precoEnvio

quantidadePedidos = int(input("Digite a quantidade de pedidos: "))

print("Valor total do envio é: R$",round(valorTotalEnvio(quantidadePedidos), 1))

