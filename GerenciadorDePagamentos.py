print('============= LOJAS RAFA ============')
valor = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
pag = int(input('Qual é a opção? '))
if pag == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - (valor * 10 /100):.2f} no final')
elif pag == 2:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - (valor * 5 / 100):.2f} no final')
elif pag ==3:
    print(f'Sua compra sera parcelada em 2x de R${valor / 2:.2f} sem juros')
    print(f'Sua compra de R${valor:.2f} vai custar R${valor:.2f} no final')
elif pag == 4:
    res = int(input('Quantas parcelas? '))
    print(f'Sua compra sera parcelada em {res}x de R${(valor + (valor * 20 / 100)) / res:.2f} com juros')
    print(f'Sua compra de R${valor:.2f} vai custar R${valor + (valor * 20 / 100)} no final')
else:
    print('Opção Invalida!!')
print('Obrigado pela preferencia e volte sempre!')
