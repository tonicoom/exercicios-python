troco = int(input("Digite o valor da compra (0 a 99 centavos): "))

moedas50 = troco // 50
moedas25 = (troco % 50) // 25
moedas10 = ((troco % 50) % 25) // 10
moedas5 =  ((troco % 50) % 25) % 10 // 5
moedas1 =  ((troco % 50) % 25) % 10 % 5

print(f"Moeda de 50: {moedas50} \nMoeda de 25: {moedas25} \nMoeda de 10: {moedas10} \nMoeda de 5: {moedas5} \nMoeda de 1: {moedas1}")