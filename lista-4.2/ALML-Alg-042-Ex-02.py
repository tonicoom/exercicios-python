valor_produtos = [4.95, 9.95, 14.95, 19.95, 24.95]

print("Sem Desconto  Com Desconto")
for i in range(0, 5):
   
    desconto = valor_produtos[i] - valor_produtos[i] * 0.6 

    print(f"  {valor_produtos[i]}             {desconto:.2f}") 



