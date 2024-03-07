precoPratoPrincipal =  float(input("Valor Prato Principal: "))
precoSobremesa = float(input("Valor Sobremesa: "))
bebida = float(input("Valor da bebida: "))

TotalValor = precoPratoPrincipal + precoSobremesa + bebida
porcentagem = TotalValor * 0.10
TotalValor += porcentagem

print(f"O valor total da comida é: R$ {TotalValor:.2f}")



