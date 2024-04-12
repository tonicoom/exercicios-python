lista_bits8 = []
lista_qnt1 = []
lista_qnt0 = []
qnt1 = 0
qnt0 = 0
contador = 0

while True:   
    contador+=1
    bits8 = input("Digite uma seguência de 8 bits (apenas entre 0 e 1): ")
    if bits8 == "":
         break
    for i in range(0, contador):   
        if len(bits8) == 8 and (bits8[i] == "0" or bits8[i] == "1"):
              lista_bits8.append(bits8)
            
        else:
            print("Não atende aos requisitos")
            break
    

paridade = input("Qual a paridade dos bits (0 e 1): ")
if paridade == "0":
    for i in range(0, contador - 1):
        lista_bits8[i] = lista_bits8[i] + "0"
        qnt1 = lista_bits8[i].count("1")
        qnt1 = int(qnt1)
        if qnt1 % 2 == 0:
            print(lista_bits8[i])
            print("Bits paridade par")
        else:
            print("Bits paridade ímpar")
            
elif paridade == "1":
    for i in range(0, contador - 1):
        for i in range(0, contador - 1):
            lista_bits8[i] = lista_bits8[i] + "1"
            qnt1 = lista_bits8[i].count("1")
            qnt1 = int(qnt1)
            if qnt1 % 2 != 0:
                print(lista_bits8[i])
                print("Bits paridade ímpar")
                        
else:
    print("Digite a paridade correta.")
        



        
        