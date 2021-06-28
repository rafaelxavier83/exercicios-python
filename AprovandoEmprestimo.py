casa =  float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
financiamento = int(input('Quantos anos de financiamento?  '))
valorPres = casa / (financiamento * 12) 
print(f'Para pegar uma casa de {casa} em {financiamento} anos a prestação sera de R${valorPres:.2f}')
if valorPres > salario * 30 / 100: 
    print('Emprestimo negado!')
else: 
    print('Emprestimo concedido!')
