import random
resultados = []
def simular_sorteio():
    resultados = []
    while True:
        resultado = random.choice(['A', 'O'])  # 'A' para cara, 'O' para coroa
        resultados.append(resultado)
        if len(resultados) >= 3:
            if resultados[-1] == resultados[-2] == resultados[-3]:
                return len(resultados)

total_sorteios = 0
for _ in range(10):
    sorteios = simular_sorteio()
    total_sorteios += sorteios
    print(' '.join(resultados), f'({sorteios} sorteios)')
media = total_sorteios / 10
print(f'\nNa média, foram necessários {media:.1f} sorteios.')
