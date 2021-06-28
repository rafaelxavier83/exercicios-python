somaIdade = 0
maiorIdadeHomem = 0
mediaIdade = 0
totMulher20 = 0
nomeVelho = ''
for c in range(1, 5):
    print(f'-----{c}º Pessoa-----')
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M/F]:  ')
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = c
        nomeVelho = c
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print(f'A media de idade do grupo é de {mediaIdade} anos.')    
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}')
print(f'Ao todo são {totMulher20} mulheres com menor de 20 anos')
