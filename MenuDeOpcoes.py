from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while True:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA''')
    op = int(input('>>>>> Qual é a sua opção? '))
    if op == 1:
        somar = n1 + n2
        print(f'O resultado de {n1} + {n2} = {somar}')
        print('='*30)
    elif op == 2:
        multiplicar = n1 * n2
        print(f'O resultado de {n1} x {n2} = {multiplicar}')
        print('='*30)
    elif op == 3:
        if n1 > n2:
            print(f'entre {n1} e {n2} o maior valor foi {n1}')
            print('='*30)
        else:
            print(f'entre {n1} e {n2} o maior valor foi {n2}')
            print('='*30)
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if op < 1 or op > 5:
        print('Opção invalida, tente novamente')       
    if op == 5:
         print('Finalizando...')
         sleep(1)
         print('Fim do programa! Volte sempre!')
         break
