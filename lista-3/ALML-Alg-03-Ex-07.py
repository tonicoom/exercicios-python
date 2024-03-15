decibeis = int(input("Digite em decibeis o barulho: "))

if decibeis > 106 and decibeis < 130:
    print("Seu barulho está entre a britadeira e o cortador de grama")
elif decibeis == 130:
    print("Britadeira")
elif decibeis == 106:
    print("Cortador de grama")

elif decibeis > 70 and decibeis < 106:
    print("Seu barulho está entre cortador de grama e despertador ")
elif decibeis == 70:
    print("Despertador")

elif decibeis > 40 and decibeis < 70:
    print("Seu barulho está entre um despertador e uma sala silenciosa ")
elif decibeis == 40:
    print("Sala silenciosa")

elif decibeis < 40:
    print("Menos barulho que uma sala silenciosa")
elif decibeis > 130: 
    print("Mais barulo que uma britadeira")