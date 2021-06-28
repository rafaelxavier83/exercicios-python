salario = float(input('Qual é o salario do funcionario? R$ '))
print(f'Um funcionario que ganhava {salario:.2f}, com 15% de aumento, passa a receber R${salario + (salario * 15 / 100):.2f}')
