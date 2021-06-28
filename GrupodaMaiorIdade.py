from datetime import date
totMaior = 0
totMenor = 0
for c in range(1, 8):
    anoNasc = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idadeAtual = date.today().year - anoNasc    
    if idadeAtual >= 18: 
        totMaior += 1   

    else:
        totMenor += 1
    
print(f'São {totMaior} pessoas maiores de idade')
print(f'São {totMenor} pessoas menores de idade')
