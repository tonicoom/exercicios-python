celsius = []
farenheit = []

print("Celcius Farenheit")
for i in range(1, 11):
    celsius.append(i * 10)
    farenheit.append(celsius[i - 1] * (9/ 5)  + 32)
    print(f"   {celsius[i -1]}     {farenheit[i-1]}")
    

 
