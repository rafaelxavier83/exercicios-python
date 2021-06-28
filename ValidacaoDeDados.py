sexo = input('Informe seu sexo: [M/F] ')
while sexo not in 'MmFf':
        sexo = input('Dados invalidos. Por favor, informe seu sexo: ')
print(f'Sexo {sexo} registrado com sucesso.')
   