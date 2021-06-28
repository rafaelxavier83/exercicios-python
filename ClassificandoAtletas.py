from datetime import date
import datetime
anoAtual = datetime.date.today().year

nasc = int(input('Ano de nascimento: ')) 

idade = anoAtual - nasc

if idade <= 9:
    print(f'idade igual a {idade}, categoria Mirim')
elif idade > 9 and idade <= 14:
    print(f'idade igual a {idade}, categoria Infantil')
elif idade > 14 and idade <= 19:
    print(f'idade igual a {idade}, categoria Junior')
elif idade > 19 and idade <= 25:
    print(f'idade igual a {idade}, categoria Senior')
elif idade > 25:
    print(f'idade igual a {idade}, categoria Master')
