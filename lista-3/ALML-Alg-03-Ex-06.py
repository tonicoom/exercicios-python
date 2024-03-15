l1 = int(input("º1 Lado: "))
l2 = int(input("º2 Lado: "))
l3 = int(input("º3 Lado: "))

if l1 == l2 and l2 == l3:
    print("Eles são equiláteros")

elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Eles são isóceles")

else:
    print("São escalenos")