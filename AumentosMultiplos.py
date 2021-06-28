salario = float(input('Qual é o salario do funcionario? R$'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'Quem ganhava R${salario} passa a ganhar R${aumento} agora')
if salario < 1250:
    aumento = salario + (salario * 15 / 100)
    print(f'Quem ganhava R${salario} passa a ganhar R${aumento} agora')
