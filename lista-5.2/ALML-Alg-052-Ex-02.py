def totalViagem(distanciaM):
    TARIFA = 4.25
    return (distanciaM / 140) * TARIFA

distanciaViagem = int(input("Digite a distância da viagem em metros: "))

print(totalViagem(distanciaViagem))