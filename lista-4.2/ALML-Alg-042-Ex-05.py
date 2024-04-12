i = True
pessoas = 0
valorTotal = 0.0

while i == True:
    idade = input("Digite a idade da pessoa: ")
    if idade == "":
        break
    idade = int(idade)

    if idade < 3:
        valorTotal+= 0

    elif idade >= 3 and idade <= 12:
        valorTotal+=14
    elif idade >= 65:
        valorTotal+=18
    else:
        valorTotal+= 23
    
    pessoas +=1

print(f"O valor referente as {pessoas} pessoas é igual a R${valorTotal:.2f}")


