print('-'*30)
print(f'{"CADASTRE UMA PESSOA"}')
print('-'*30)
pessMais18 = cdasHomens = mulherMenos20 = 0
while True:    
    idade = int(input('IDADE: '))    
    sexo = ' '
    while sexo not in 'MF':    
        sexo = str(input('SEXO: [M/F] ')).strip().upper()[0] 
    if idade > 18:
        pessMais18 += 1            
    if sexo == 'M':
        cdasHomens += 1
    if sexo == 'F' and idade < 20:
            mulherMenos20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] 
    if resp == 'N':
        break     
print(f'Total de pessoas com mais de 18 anos: {pessMais18}')
print(f'Ao todo temos {cdasHomens} homens cadastrados.')
print(f'E temos {mulherMenos20} mulheres com menos de 20 anos.')
