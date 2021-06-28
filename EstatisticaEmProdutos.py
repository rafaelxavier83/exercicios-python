print('-'*40)
print(f'{"LOJA SUPER BARATÂO":^40}')
#print('{:^40}'.format('LOJA SUPER BARATÂO'))
print('-'*40)
totgasto = qtd = menor = cont = 0
barato = ' '
while True:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    totgasto += preco
    if preco > 1000:
        qtd += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${totgasto:.2f}')
print(f'Temos {qtd} produtos custando mais de R$1000.00')
print(f'O Produto mais barato foi {barato} que custa R${menor:.2f}')
