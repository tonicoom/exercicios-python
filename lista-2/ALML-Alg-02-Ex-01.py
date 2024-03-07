print("Unidade de Tempo")
dias = int(input("Dias: "))
horas = int(input("Horas: ")) 
minutos = int(input("Minutos: "))

diasEmSegundos = dias * 86400
horasEmSegundos = horas * 3600
minutosEmSegundos = minutos * 60

segundosTotais = diasEmSegundos + horasEmSegundos + minutosEmSegundos

print("Total de segundos é: ",segundosTotais)