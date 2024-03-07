matricula = int(input("Digite a sua matrícula: "))
#182034
semestre = (matricula % 10000) // 1000
ano = matricula // 10000
print("Semestre: ", semestre)
print("Ano: ", ano)
