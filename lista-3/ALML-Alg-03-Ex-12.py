ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    print("Ano é bisexto")
    
elif ano % 100 == 0:
    print("Não é bisexto")

elif ano % 4 == 0:
    print("Ano é bisexto")

else:
    print("Não é bisexto")


