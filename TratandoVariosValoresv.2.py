num = cont = soma = 0
num = int(input('Digite um numero [999 para parar] '))
while num != 999:    
    soma += num
    cont += 1    
    num = int(input('Digite um numero [999 para parar] '))
print(f'Você digitou {cont -1} numeros e a soma entre eles é {soma}')
