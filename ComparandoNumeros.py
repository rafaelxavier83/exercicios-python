n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O primeiro valor é maior')
if n2 > n1:
    print('O segundo valor é maior')
else:
    if n1 == n2:
        print('Não existe valor maior, os dois são iguais')
