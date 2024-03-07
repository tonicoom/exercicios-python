print("Unidades de tempo")
segundos = int(input("Segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 86400) % 3600 // 60 
segundos = (segundos % 86400) % 3600 % 60


print(f"{dias:02} : {horas:02} : {minutos:02} : {segundos:02}")
