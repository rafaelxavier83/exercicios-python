soma = 0
cont = 0
for conta in range(1, 501, 2):
    if conta % 3 == 0:
        cont += 1
        soma += conta 
print(f'A soma de todos os {cont} valores solicitados é {soma}')
