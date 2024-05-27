def encaixa(a, b):
    a = str(a)
    b = str(b)
    
    return a[-len(b): ] == b

   

print(encaixa(123, 123))

 