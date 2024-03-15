print("Número de dias do mês")
mes = input("Digite o nome do mês: ")

if mes == "Janeiro" or mes == "Março" or mes == "Maio" or mes == "Julho" or mes == "Agosto" or mes == "Outubro" or mes == "Dezembro":
    print("31 dias")
elif mes == "Junho" or mes == "Setembro" or mes == "Novembro":
    print("30 dias")
elif mes == "Fevereiro":
    print("28 ou 29 dias")

else:
    print("Digite a primeira letra maiúscula e verifique se a palavra que você escreveu está correta.")
