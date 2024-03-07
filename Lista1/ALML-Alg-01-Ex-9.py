valorDepositado = float(input("Digite o valor depositado: "))

umAnoValor = valorDepositado * 0.12
valorDepositado += umAnoValor
print(f"Valor 1 anos de deposito: R$ {valorDepositado:.2f}")

umDoisValor = valorDepositado * 0.12
valorDepositado += umAnoValor
print(f"Valor 2 anos de deposito: R$ {valorDepositado:.2f}")

umTresValor = valorDepositado * 0.12
valorDepositado += umAnoValor
print(f"Valor 3 anos de deposito: R$ {valorDepositado:.2f}")

