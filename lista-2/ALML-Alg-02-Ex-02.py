print("Unidades de tempo")
segundos = int(input("Segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 60 // 60
minutos = (segundos % 86400) % 60 // 60 
segundos = (segundos % 86400) % 60 % 60


print(f"{dias} {horas} {minutos} {segundos}")
