n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'sua media foi {media:.1f}, Reprovado!')
elif media >= 5 and media < 6.9:
    print(f'sua media foi {media:.1f}, Recuperação!')
elif media > 7:
    print(f'sua media foi {media:.1f}, Aprovado')
