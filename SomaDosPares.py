soma = 0
for num in range(1, 7):
    n = int(input(f'Digite o {num}º valor: '))
    if n % 2 == 0:
        soma += n         
print(f' A soma dos numeros pares é {soma}')   
