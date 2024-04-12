nbinario = input("Digite o número binário: ")
ndecimal = 0

for i in range(0, len(nbinario)):
    ndecimal += int(nbinario[i]) * (2 ** i)

print(ndecimal)
