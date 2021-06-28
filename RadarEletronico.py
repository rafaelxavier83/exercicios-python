veloc = int(input('Qual a velocidade atual do carro? '))
if veloc > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h')
    print(f'Você deve pagar uma multa de R${(veloc - 80) * 7:.2f}!')
print('Tenha um bom dia! Dirija com segurança.')
