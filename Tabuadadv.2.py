num = int(input('Digite um numero para ver sua tabuada: '))
for tab in range(1, 11):    
    result = num * tab    
    print(f'{num} x {tab:2} = {result}')
