qtddia = int(input('Quantos dias alugados? '))
qtdKm = int(input('Quantos km rodados? '))
dia = qtddia * 60
km =  qtdKm * 0.15
total = dia + km
print(f'O total a pagar foi {total:.2f}')
