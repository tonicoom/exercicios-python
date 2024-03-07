data =  int(input("Digite o alguma data: "))

dia = data // 10000
mes = ((data // 100) % 1000) % 100
ano = ((data % 100000) % 10000) % 100

print(f"{ano:02} / {mes:02} / {dia:02}")


