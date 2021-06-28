soma = qtd = media = maior = menor = 0
res = 'S'
while res in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    qtd += 1
    res = input('Quer continuar? [S/N] ')    
    if qtd == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / qtd
print(f'Você digitou {qtd} numeros, a soma deu {soma} e a media foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
