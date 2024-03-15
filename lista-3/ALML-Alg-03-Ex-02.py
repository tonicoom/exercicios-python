print("Conversor de Anos Caninos")
idadeCanina = int(input("Digite a idade do seu cachorro: "))
if idadeCanina <= 2 and idadeCanina > 0:
    idadeCanina = idadeCanina * 10.5
    print(f"{idadeCanina} anos")

elif idadeCanina > 2:
    idadeCanina = idadeCanina - 2
    idadeCanina = idadeCanina * 4
    idadeCanina = idadeCanina + 21
    print(f"{idadeCanina}anos")

else:
    print("Digite um número maior que zero.")
    