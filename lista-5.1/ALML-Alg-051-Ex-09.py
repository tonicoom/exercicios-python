def eh_bissesto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False
    
print(
eh_bissesto(2024),
eh_bissesto(2043),
eh_bissesto(2028)
)